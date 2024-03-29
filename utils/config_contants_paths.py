#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os

# ---------------------------- CONSTANTS -----------------------------

PERSON_QUANTITY = 100

TOTAL_TRIES = 3
WAIT_TIME_MINUTES = 2

WEBHOOK_WAIT_TIME = 3
DAYS_OF_DUE_DATE = 3

SLEEP_TIME_ZERO = 0
SLEEP_TIME_ONE = 1     # 1 minute
SLEEP_TIME_TWO = 2     # 2 minute
SLEEP_TIME_THREE = 3   # 3 minute

HEADER_PIPE_SEPARATOR = '|'
HEADER_COMMER_SEPARATOR = ','

MIN_LIMIT = 1
MAX_LIMIT = 100

FILE_OPERATION_TYPE = {
    "read": "a",
    "write": "w",
    "add new": "a",
    "write binary file": "wb",
}


# ------------------------------- PATHS -------------------------------

IJDEVLIBS = 'IJDevLibs'
IJDEVLIBS_SPLIT = f'/{IJDEVLIBS}'


RANDOM_PERSON_FILE_PATH = 'stage/FILES_DIR/RANDOM_PERSON.text'


CURRENT_WORK_SPACE = os.getcwd()


# --------------------------- CLASSES ----------------------------------


class HoldSomeThing:

    def __init__(self, some_obj):
        self.__something__ = some_obj

    # Getter
    def get_some(self):
        return self.__something__

    # Setter
    def set_some(self, something):
        self.__something__ = something


# ----------------------- API CREDENTIALS -------------------------------

# remove thsi line at the end

# NGROK_API_KEY = '<NGROK_API_KEY>'


__api_credentials__ = {
    "ngrok_api_key": "2CJOZXfRZdJOZABSJo6g9wXcF9o_6BKYhps9j62ggdLUJHSPV",
    "api_name 1": "key or token 1",
    "api_name 2": "key or token 2",
    "api_name 3": "key or token 3",
    "api_name 4": "key or token 4",
}

APP_INFO = """
    This is the package I use to help me on my projects.
    This package contain several functions to build any application you as a Dev need.
"""