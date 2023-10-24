import logging
import json

def initiate_logger(file):
    logger = logging.getLogger(__name__)
    logging.getLogger().setLevel(logging.DEBUG)

    handler = logging.FileHandler(file)
    file_handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    
    file_handler.setFormatter(formatter)
    handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(handler)

    return logger

def validate_key(logger, api_key, secret_key):
    '''
    Validate that both keys have 64 char length.
    '''

    if len(api_key) + len(secret_key) != 128:
        logger.exception('Failed Validation.')
        raise
    return

def print_json(json_obj):
    return print(json.dumps(json_obj, indent=4))