import logging

from common.consts import LOG_FILE_PATH

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M',
                    handlers=[logging.FileHandler(LOG_FILE_PATH), logging.StreamHandler()])

def info(msg: str): 
    logging.info(msg)

def error(msg: str): 
    logging.error(msg)

def trim_log_file(max_lines=500):
    try:
        with open(LOG_FILE_PATH, 'r') as file:
            lines = file.readlines()

        if len(lines) > max_lines:
            with open(LOG_FILE_PATH, 'w') as file:
                file.writelines(lines[-max_lines:])
    except Exception as e:
        print(f"Error trimming log file: {e}")