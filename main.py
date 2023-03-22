from watch import monitor_folder
from load_config import load_config
import sys


def main():
    """Run monitoring new files in PATH"""
    monitor_folder(load_config("target_folder")) if load_config("target_folder") else sys.exit()


if __name__ == "__main__":
    main()
