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


def format_number(curr_num, match_num):

    curr_num_str = f'{curr_num}'
    match_num_str = f'{match_num}'

    if '.' in match_num_str:
        match_dec = len(match_num_str.split('.')[1])
        curr_num_str = f'{curr_num:.{match_dec}f}'
        curr_num_str = curr_num_str[:]
    else:
        return f'{int(curr_num)}'
    
    return curr_num_str