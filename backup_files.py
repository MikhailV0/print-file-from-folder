import shutil
import os
from time import strftime


def backup_file(path: str) -> bool:
    """Move file to backup folder"""
    time_name: str = strftime("%d%m%Y_%S-")
    backup_file_path: str = "\\".join(path.split('\\')[:-1]) + "\\backup\\" + time_name + path.split("\\")[-1]
    backup_path: str = "\\".join(path.split('\\')[:-1]) + "\\backup"
    print("\\".join(path.split('\\')[:-1]) + "\\backup\\" + path.split("\\")[-1])
    if os.path.isdir(backup_path):
        shutil.move(path, backup_file_path)
        return True
    elif not os.path.isdir(backup_path):
        os.mkdir(backup_path)
        shutil.move(path, backup_file_path)
        return True
    else:
        return False

