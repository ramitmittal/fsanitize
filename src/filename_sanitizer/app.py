import sys
import os

from filename_sanitizer import logmgr
from filename_sanitizer import sanitize

class InvalidDirError(Exception):
    """There was a problem with the provided directory path"""


def main():
    try:
        if os.path.exists(sys.argv[1]):
            logmgr.initialize_logger()
            sanitize.recursive_rename(sys.argv[1])
        else:
            raise InvalidDirError
    except (IndexError, InvalidDirError):
        print("Please provide a valid directory path as first argument.")
        sys.exit(1)
        

if __name__ == '__main__':
    main()
