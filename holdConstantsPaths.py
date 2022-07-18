#!src/bin/env python3
# encoding: utf-8


import os


# ---------------------------------------------------------

class HoldSomeThing:

    def __init__(self, some_obj):
        self.__some_sent = some_obj

    # Getter
    def get_some_sent(self):
        return self.__some_sent

    # Setter
    def set_some_sent(self, something):
        self.__some_sent = something


# contants goes here

SLEEP_TIME_ZERO = 0
SLEEP_TIME_ONE = 1     # 1 minute
SLEEP_TIME_TWO = 2     # 2 minute
SLEEP_TIME_THREE = 3   # 3 minute

HEADER_PIPE_SEPARATOR = '|'
HEADER_COMMER_SEPARATOR = ','

CURRENT_WORK_SPACE = os.getcwd()

FILE_OPERATION_TYPE = {
    "read": "a",
    "write": "w",
    "add new": "a",
    "write binary": "wb",
}

MIN_LIMIT = 1
MAX_LIMIT = 100

# paths goes here

IJGU_PACKAGE = 'IJGeneralUsagePackage/'
