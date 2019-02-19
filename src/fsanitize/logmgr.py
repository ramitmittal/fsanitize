import logging
import os

logger = logging.getLogger()


def initialize_logger():
    """
    Initialize application logger.
    """

    log_file_path = os.path.join(os.path.dirname(os.getcwd()), 'rename_log')
    log_file_handler = logging.FileHandler(log_file_path)
    logger.addHandler(log_file_handler)
    logger.setLevel(logging.INFO)
