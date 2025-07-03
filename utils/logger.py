import logging
import sys
import os
from logging.handlers import RotatingFileHandler

loggers = {}

def get_logger(name, log_file='app.log'):
    global loggers

    if loggers.get(name):
        return loggers.get(name)

    # Create logs directory if it doesn't exist
    log_dir = 'logs'
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    log_path = os.path.join(log_dir, log_file)

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Console handler
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setLevel(logging.INFO)
    stream_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    stream_handler.setFormatter(stream_formatter)
    
    # File handler
    file_handler = RotatingFileHandler(log_path, maxBytes=10*1024*1024, backupCount=5) # 10MB per file, 5 backups
    file_handler.setLevel(logging.DEBUG)
    file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(file_formatter)

    if not logger.handlers:
        logger.addHandler(stream_handler)
        logger.addHandler(file_handler)

    loggers[name] = logger
    return logger
