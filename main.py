from watch import monitor_folder


def main():
    """Run monitoring new files in PATH"""
    monitor_folder(PATH)


if __name__ == "__main__":
    PATH: str = "M:\\test"
    main()
