import os
import shutil

# Folder to organize
SOURCE_FOLDER = r"D:\Downloads"



# File categories
FILE_TYPES = {
    "Images": [
        ".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".tiff", ".heic"
    ],
    "Videos": [
        ".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv", ".webm", ".m4v"
    ],
    "Music": [
        ".mp3", ".wav", ".aac", ".ogg", ".flac", ".m4a"
    ],
    "Documents": [
        ".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx",
        ".txt", ".csv", ".rtf"
    ],
    "Archives": [
        ".zip", ".rar", ".7z", ".tar", ".gz", ".bz2"
    ],
    "ISO": [
        ".iso", ".img"
    ],
    "Programs": [
        ".exe", ".msi", ".bat"
    ],
    "Scripts": [
        ".py", ".ps1", ".js", ".vbs", ".cmd"
    ],
    "Torrents": [
        ".torrent"
    ]
}

