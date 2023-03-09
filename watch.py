import os.path
from print_files import print_file
from backup_files import backup_file
import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class MonitorFolder(FileSystemEventHandler):
    def on_created(self, event):
        # print(event.src_path, event.event_type)
        if os.path.isfile(event.src_path):
            print_file(event.src_path)
            time.sleep(5)
            backup_file(event.src_path)


def monitor_folder(path: str):
    """Monitoring new files in path, and print it"""
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
