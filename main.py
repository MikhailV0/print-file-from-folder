from watch import monitor_folder
from load_config import load_config


def main():
    """Run monitoring new files in PATH"""
    monitor_folder(load_config(1)) if load_config(1) else exit()


if __name__ == "__main__":
    main()
