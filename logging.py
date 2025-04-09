

import logging
import os

CreateLog = True
log_level = logging.INFO
log_file_name = 'log.log'

def configure_logging():
    if not os.path.exists(os.path.dirname(log_file_name)):
        os.makedirs(os.path.dirname(log_file_name))
    if not os.access(os.path.dirname(log_file_name), os.W_OK):
        raise Exception(f"Cannot write to log file {log_file_name}")
    logging.basicConfig(filename=log_file_name, level=log_level, format='%(asctime)s - %(message)s')

def lw(message):
    if CreateLog:
        try:
            print(message)
            logging.info(message)
        except Exception as e:
            print(f"Error logging message: {e}")

if CreateLog:
    configure_logging()