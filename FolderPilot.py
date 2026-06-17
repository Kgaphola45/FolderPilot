import argparse
import os
import shutil

DEFAULT_SOURCE_FOLDER = r"D:\Downloads"


FILE_TYPES = {
    "Images": [
        ".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".tiff", ".heic",
        ".raw", ".cr2", ".nef", ".arw", ".dng", ".ico",
    ],
    "Videos": [
        ".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv", ".webm", ".m4v",
        ".mpeg", ".mpg", ".3gp", ".mts", ".m2ts",
    ],
    "Music": [
        ".mp3", ".wav", ".aac", ".ogg", ".flac", ".m4a", ".wma", ".alac", ".aiff",
    ],
    "Documents": [
        ".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx",
        ".txt", ".csv", ".rtf", ".odt", ".ods", ".odp", ".md", ".json",
        ".xml", ".html", ".htm", ".log", ".epub",
    ],
    "Archives": [
        ".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz",
    ],
    "ISO": [
        ".iso", ".img", ".dmg",
    ],
    "Programs": [
        ".exe", ".msi", ".bat", ".app", ".apk", ".deb", ".pkg",
    ],
    "Scripts": [
        ".py", ".ps1", ".js", ".vbs", ".cmd", ".sh", ".ts", ".rb",
        ".php", ".pl", ".go", ".lua", ".c", ".cpp", ".cs", ".java",
    ],
    "Torrents": [
        ".torrent",
    ],
}

COMPOUND_EXTENSIONS = {
    ".tar.gz": "Archives",
    ".tar.bz2": "Archives",
    ".tar.xz": "Archives",
    ".iso.gz": "Archives",
}

TARGET_FOLDERS = set(FILE_TYPES) | {"Others"}


def get_destination_folder(item_name):
    lower_name = item_name.lower()

    for compound_extension, category in COMPOUND_EXTENSIONS.items():
        if lower_name.endswith(compound_extension):
            return category

    extension = os.path.splitext(lower_name)[1]

    for category, extensions in FILE_TYPES.items():
        if extension in extensions:
            return category

    return "Others"


def split_name_and_extension(item_name):
    lower_name = item_name.lower()

    for compound_extension in COMPOUND_EXTENSIONS:
        if lower_name.endswith(compound_extension):
            return item_name[: -len(compound_extension)], item_name[-len(compound_extension) :]

    return os.path.splitext(item_name)


def get_items(folder, recursive):
    if not recursive:
        return sorted(os.path.join(folder, item) for item in os.listdir(folder))

    items = []
    for root, dirs, files in os.walk(folder):
        dirs[:] = [directory for directory in dirs if directory not in TARGET_FOLDERS]
        for file_name in files:
            items.append(os.path.join(root, file_name))

    return sorted(items)


def organize_folder(folder, recursive=False, dry_run=False):
    if not os.path.isdir(folder):
        raise NotADirectoryError(f"Folder does not exist or is not a directory: {folder}")

    for item_path in get_items(folder, recursive):
        item = os.path.basename(item_path)

        if os.path.isdir(item_path):
            continue

        if os.path.basename(os.path.dirname(item_path)) in TARGET_FOLDERS:
            continue

        destination_folder = get_destination_folder(item)
        category_path = os.path.join(folder, destination_folder)
        os.makedirs(category_path, exist_ok=True)

        destination = os.path.join(category_path, item)

        if os.path.exists(destination):
            name, ext = split_name_and_extension(item)
            counter = 1

            while True:
                new_name = f"{name}_{counter}{ext}"
                destination = os.path.join(category_path, new_name)

                if not os.path.exists(destination):
                    break

                counter += 1

        if dry_run:
            print(f"Would move: {item} -> {destination_folder}")
            continue

        shutil.move(item_path, destination)
        print(f"Moved: {item} -> {destination_folder}")


def parse_args():
    parser = argparse.ArgumentParser(description="Organize files into category folders.")
    parser.add_argument(
        "folder",
        nargs="?",
        default=DEFAULT_SOURCE_FOLDER,
        help="Folder to organize",
    )
    parser.add_argument(
        "--recursive",
        action="store_true",
        help="Organize files inside subfolders too",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be moved without changing files",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    organize_folder(args.folder, recursive=args.recursive, dry_run=args.dry_run)
    print("\nOrganization completed!")