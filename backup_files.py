import shutil
import os
from time import strftime
import logging.config

logging.config.fileConfig('loging.conf', disable_existing_loggers=False)
logger = logging.getLogger(__name__)


def backup_file(path: str) -> bool:
    """Move file to back up folder"""
    backup_folder = os.path.join(os.path.dirname(path), 'backup')
    if not os.path.isdir(backup_folder):
        try:
            os.mkdir(backup_folder)
        except PermissionError:
            logger.critical(f'Error create folder {backup_folder}: permission denied')
            return False
    backup_filename = strftime("%d-%m-%Y-%H-%M-%S-") + os.path.basename(path)
    backup_path = os.path.join(backup_folder, backup_filename)
    if os.path.exists(backup_path):
        logger.error(f'Backup file {backup_path} already exists')
        return False
    try:
        shutil.move(path, backup_path)
        return True
    except PermissionError:
        logger.critical(f'Error moving {path} to {backup_path}: permission denied')
        return False
    except FileNotFoundError:
        logger.critical(f'Error moving {path} to {backup_path}: file not found')
        return False
