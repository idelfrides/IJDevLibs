#!src/bin/env python3
# encoding: utf-8


from time import sleep
import os

# contants goes here

SLEEP_TIME_ZERO = 0
SLEEP_TIME_ONE = 1     # 1 minute
SLEEP_TIME_TWO = 2     # 2 minute
SLEEP_TIME_THREE = 3   # 3 minute


HEADER_PIPE_SEPARATOR = '|'
HEADER_COMMER_SEPARATOR = ','
CURRENT_WORK_SPACE = os.getcwd()

OPERATION_TYPE = {
    "read": "a",
    "write": "w",
    "add new": "a",
    "write binary": "wb",
}


# paths goes here

IJGU_PACKAGE = 'IJGeneralUsagePackage/'
