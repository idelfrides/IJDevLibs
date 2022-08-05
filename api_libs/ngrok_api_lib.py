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


    __BASE_URL__  = 'https://api.ngrok.com/{}'


    def __init__(self) -> None:

        self.__rest_header__ = {
            'Authorization': 'Bearer {}'.format(__api_credentials__['ngrok_api_key']
            ),
            'Content-Type': 'application/json',
            'Ngrok-Version': '2'
        }


    def get_ngrok_entity(self, endpoint):
        print_log(f'GETTING NGROK ENTITY [ {endpoint} ] . . .')

        rest_url = self.__BASE_URL__.format(endpoint)

        ngrok_public_url = ''

        try_number = 1
        while try_number <= TOTAL_TRIES:

            print_log(f'TRYING: [ {try_number} ]')

            # CHANGE THIS
            try:
                payload = requests.get(rest_url, headers=self.__rest_header__)
            except Exception as error:
                print_log(f'EXCEPTION : {error}')
                print_log(f'WAITTING {WAIT_TIME_MINUTES}  minutes')
                time.sleep(self.WAIT_TIME_MINUTES*60)

            # ---------

            if payload.status_code == 200:
                break
            else:
                print_log(f'WAITTING {self.wait_time} minutes')
                time.sleep(WAIT_TIME_MINUTES*60)

            try_number += 1
            if try_number  > TOTAL_TRIES:
                print_log(f'TRIES COMPLETED: NO [ {endpoint} ] TO GET')
                return ngrok_public_url

        paylod_content = payload.json()

        ngrok_public_url = paylod_content.get('tunnels')[0]['public_url']

        print_log(f'GETTING NGROK [{endpoint}] DONE')

        return ngrok_public_url
