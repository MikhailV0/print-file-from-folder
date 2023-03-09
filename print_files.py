import win32print
import win32api
import pywintypes
import sys


def print_file(input_pdf):
    """Print file on default system printer"""
    name: str = win32print.GetDefaultPrinter()
    try:
        win32api.ShellExecute(0, "print", f'{input_pdf}', None, ".", 0)
        return True
    except pywintypes.error:
        print("COM Error")
        return False


if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else input("Enter file path: ")
    print_file(path)
