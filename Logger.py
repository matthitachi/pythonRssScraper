import logging


class logger:
    def __init__(self, filename=None):
        if not filename:
            filename = 'app-log.txt'
        logging.basicConfig(filename=filename, level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s',  datefmt='%d-%b-%y %H:%M:%S')
        # logging.warning('This will get logged to a file')

    def debug(self, message):
        logging.debug(message)

    def info(self, message):
        logging.info(message)

    def warning(self, message):
        logging.warning(message)

    def error(self, message):
        logging.error(message)

    def critical(self, message):
        logging.critical(message)