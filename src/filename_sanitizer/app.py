import easyargs
from filename_sanitizer import logmgr
from filename_sanitizer import sanitize


@easyargs
def main(directory):
    logmgr.initialize_logger()
    sanitize.recursive_rename(directory)


if __name__ == '__main__':
    main()
