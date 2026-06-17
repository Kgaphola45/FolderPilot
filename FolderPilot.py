import os
import shutil

# Folder to organize
SOURCE_FOLDER = r"D:\Downloads"



# File categories
FILE_TYPES = {
    "Images": [
        ".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".tiff", ".heic",
        ".raw", ".cr2", ".nef", ".arw", ".dng", ".ico"
    ],
    "Videos": [
        ".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv", ".webm", ".m4v",
        ".mpeg", ".mpg", ".3gp", ".ts", ".mts", ".m2ts"
    ],
    "Music": [
        ".mp3", ".wav", ".aac", ".ogg", ".flac", ".m4a", ".wma", ".alac", ".aiff"
    ],
    "Documents": [
        ".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx",
        ".txt", ".csv", ".rtf", ".odt", ".ods", ".odp", ".md", ".json",
        ".xml", ".html", ".htm", ".log", ".epub"
    ],
    "Archives": [
        ".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz", ".iso.gz"
    ],
    "ISO": [
        ".iso", ".img", ".dmg"
    ],
    "Programs": [
        ".exe", ".msi", ".bat", ".app", ".apk", ".deb", ".pkg"
    ],
    "Scripts": [
        ".py", ".ps1", ".js", ".vbs", ".cmd", ".sh", ".ts", ".rb",
        ".php", ".pl", ".go", ".lua", ".c", ".cpp", ".cs", ".java"
    ],
    "Torrents": [
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

if __name__ == "__main__":
    organize_folder(SOURCE_FOLDER)
    print("\nOrganization completed!")