import os
import shutil
import argparse

DEFAULT_SOURCE_FOLDER = r"D:\Downloads"



# File categories
FILE_TYPES = {
    "Images": [
        ".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".tiff", ".heic",
        ".raw", ".cr2", ".nef", ".arw", ".dng", ".ico"
    ],
    "Videos": [
        ".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv", ".webm", ".m4v",
        ".mpeg", ".mpg", ".3gp", ".mts", ".m2ts"
    ],
    "Music": [
        ".mp3", ".wav", ".aac", ".ogg", ".flac", ".m4a", ".wma", ".alac", ".aiff"
    ],
    "Documents": [

COMPOUND_EXTENSIONS = {
    ".tar.gz": "Archives",
    ".tar.bz2": "Archives",
    ".tar.xz": "Archives",
    ".iso.gz": "Archives",
}


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
        ".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx",

def organize_folder(folder, recursive=False):
    if recursive:
        items = []
        for root, _, files in os.walk(folder):
            for file_name in files:
                items.append(os.path.join(root, file_name))
    else:
        items = [os.path.join(folder, item) for item in os.listdir(folder)]

    for item_path in items:
        item = os.path.basename(item_path)
        ".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz", ".iso.gz"
    ],
    "ISO": [
        ".iso", ".img", ".dmg"
    ],
        destination_folder = get_destination_folder(item)
        ".torrent"
    ]
}

def organize_folder(folder):
    for item in os.listdir(folder):
        item_path = os.path.join(folder, item)

        # Skip folders
        if os.path.isdir(item_path):
            continue

        extension = os.path.splitext(item)[1].lower()
        destination_folder = "Others"

        # Find matching category
        for category, extensions in FILE_TYPES.items():
            if extension in extensions:
                destination_folder = category
                break

        category_path = os.path.join(folder, destination_folder)
        os.makedirs(category_path, exist_ok=True)

        destination = os.path.join(category_path, item)

        # Handle duplicate names
        if os.path.exists(destination):
            name, ext = os.path.splitext(item)
            counter = 1

            while True:
                new_name = f"{name}_{counter}{ext}"
                destination = os.path.join(category_path, new_name)

                if not os.path.exists(destination):
                    break

                counter += 1

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
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    organize_folder(args.folder, recursive=args.recursive)
    print("\nOrganization completed!")