"""This module monitors a folder and performs actions"""


import os.path
from print_files import print_file
from backup_files import backup_file
from load_config import load_config
import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import logging.config

logging.config.fileConfig('loging.conf', disable_existing_loggers=False)
logger = logging.getLogger(__name__)


class MonitorFolder(FileSystemEventHandler):
    def on_created(self, event):
        #get filename and file_extension to diff variable
        filename, file_extension = os.path.splitext(event.src_path)
        if file_extension != '.part' and file_extension.lstrip('.') in (load_config('file_extensions')).split(','):
            file_handler(event.src_path)
    def on_moved(self, event):
        # Linux when copy to smb create temp *.part then rename file
        filename, file_extension = os.path.splitext(event.dest_path)
        if file_extension.lstrip('.') in (load_config('file_extensions')).split(','):
            file_handler(event.dest_path)


def file_handler(file_path: str) -> None:
    if os.path.isfile(file_path):
        # timeout for smb share folders //test mode//
        time.sleep(5)
        if print_file(file_path):
            logger.info(f'File {file_path} has been sent for printing')
            time.sleep(15)
            if backup_file(file_path):
                logger.info(f'File {file_path} has been moved')
        else:
            logger.warning(f'Something went wrong with the file {file_path}')


def monitor_folder(path: str):
    """Monitoring new files in path, and print it"""
    logger.info('monitoring started')
    event_handler = MonitorFolder()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()
    try:
        while True:
            # Set the thread sleep time
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == "__main__":
    # Set format for displaying path
    path: str = sys.argv[1] if len(sys.argv) > 1 else '.'
    monitor_folder(path)
