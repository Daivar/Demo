# calculator.py

import logging

formatter = logging.Formatter('%(asctime)s : %(name)s : %(message)s')

main_file_logger = logging.FileHandler('..\\logs\\main.log')
main_file_logger.setFormatter(formatter)
main_file_logger.setLevel(logging.INFO)

error_file_logger = logging.FileHandler('..\\logs\\error.log')
error_file_logger.setFormatter(formatter)
error_file_logger.setLevel(logging.ERROR)

logger = logging.getLogger(__name__)
logger.addHandler(main_file_logger)
logger.addHandler(error_file_logger)

class Calculator:
    def __init__(self):
        logger.info('Calculator instance created')

    def add(self, i, j):
        return i + j

    def multiply(self, i, j):
        return i * j

    def divide(self, i, j):
        try:
            return i / j
        except ZeroDivisionError as e:
            # logger.error('Division by 0')
            logger.exception('Division by 0')
