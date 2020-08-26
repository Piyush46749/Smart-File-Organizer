#import all the required packages

from pathlib import Path
from sys import argv
from shutil import move

def get_dir(filename):
    """
        This function takes filename and returns name of the
        parent directory of the respective filename
        Returns Miscellaneous if Parent is not found
    """
    ext = filename.suffix[1:]
    return dirs.get(ext, "Miscellaneous")

dirs = {
    # Images
    "jpeg": "Images",
    "png": "Images",
    "jpg": "Images",
    "tiff": "Images",
    "gif": "Images",

    # Videos
    "mp4": "Videos",
    "mkv": "Videos",
    "mov": "Videos",
    "webm": "Videos",
    "flv": "Videos",

    # Music
    "mp3": "Music",
    "ogg": "Music",
    "wav": "Music",
    "flac": "Music",