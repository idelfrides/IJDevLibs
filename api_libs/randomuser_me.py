#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""
    # This module is the ngrok lib to coonsume thrier API.

"""

import requests
import time

from utils.config_contants_paths import (
    __api_credentials__,
    TOTAL_TRIES,
    WAIT_TIME_MINUTES
)

from ..IJGeneralLib import (
    print_log
)

class NgrokAPI(object):
    """# Ngrok API entity"""


    __BASE_URL__  = 'https://randomuser.me/api/{}'


    def __init__(self) -> None:

        self.__rest_header__ = {
            'Authorization': 'Bearer {TOKEN}',
            'Content-Type': 'application/json',
        }


    def get_random_user_api(self):
        """
        Retun
            --> user_full_name
            --> user_content

        """

        print_log(f'GETTING ONE USER FROM API ...')


        try:
            payload = requests.get(self.__BASE_URL__)
        except Exception as error:
            print_log(f'EXCEPTION OCCORRED {error} \n\nGOING TO USE DEFAULT_PERSON_NAME \n\n')
            return None, None

        payload_content = payload.json()
        user_data = payload_content['results'][0]['name']

        user_full_name = (
            user_data['title'] + ' ' + user_data['first'] + ' ' + user_data['last']
        )

        user_content = f'USER: {user_full_name}'

        print_log(f'DONE')
        return user_full_name, user_content
