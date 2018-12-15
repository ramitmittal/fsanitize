import sys
import os

from fsanitize import logmgr
from fsanitize import sanitize


def main():
    """
    Main entry point for app.

    Requires path name as command line argument.
    """

    try:
        # IndexError if no argument
        path_name = sys.argv[1]

        # False if path does not exist
        if os.path.exists(path_name):
            logmgr.initialize_logger()
            sanitize.recursive_rename(sys.argv[1])
        else:
            print("Provided path does not exist. Exiting")
            sys.exit(1)

    except (IndexError):
        print("Please provide a valid directory path as first argument.")
        sys.exit(1)


if __name__ == '__main__':
    main()
