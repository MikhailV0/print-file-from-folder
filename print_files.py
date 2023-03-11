import win32api
import pywintypes
import sys
import logging.config

logging.config.fileConfig('loging.conf', disable_existing_loggers=False)
logger = logging.getLogger(__name__)


def print_file(input_file: str) -> bool:
    """Print file on default system printer"""
    try:
        win32api.ShellExecute(0, "print", f'{input_file}', None, ".", 0)
        return True
    except pywintypes.error as e:
        logger.warning(f'Printing file {input_file} failed')
        logger.exception(e)
        return False


if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else input("Enter file path: ")
    print_file(path)
