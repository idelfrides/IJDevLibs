#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""
    # This module is the ngrok lib to coonsume thrier API.

"""

import requests
import time
from lib_manager import write_content_infile

from utils.config_contants_paths import (
    PERSON_QUANTITY,
    __api_credentials__,
    TOTAL_TRIES,
    WAIT_TIME_MINUTES
)

from ..IJGeneralLib import (
    print_log
)

class BrazilianGeneratorAPI(object):
    """# Brazilian Generator API"""


    __BASE_URL__  = 'https://geradorbrasileiro.com/api/faker/'

    def __init__(self) -> None:

        self.__rest_header__ = {
            'Authorization': 'Bearer {API TOKEN',
            'Content-Type': 'application/json',
        }


    def brasilian_api_generator(self, type_data, quantity):

        rest_url = '/'.join([self.__BASE_URL__, type_data])

        url_params = {
            'limit': quantity
        }

        try:
            payload = requests.get(rest_url, params=url_params)
        except Exception as error:
            print_log(f'EXCEPTION: {error}')
            return []

        _content_ = payload.json()

        return _content_.get('values')


    def brasilian_api_generator_tofile(self, **kwargs):

        """
        # Generate random brasilian person
        ---

        ##### Generate random brasilian person data like , NAME, CPF, MOTHER, FATHER, PHONE, ADRESS, WEBSITISE, ... For our propose, we going to need only NAME nad CPF.

        ##### Informe values for all paramters separated with comma.

        ### Required parameters

            * type_data='TYPE DATA', can be [pessoa, cpf, cnpj, cnh, ...].  Default = pessoa\n
            * quantity='QUANTITY NUMBER', interger > 0. Default = 100\n
            * distiny_dir='DISTINY DIR'
            * file_name='FILE NAME',
            * operation_type='OPERATION TYPE' . Can be 'w', 'a'. Default = 'a'


        """

        persons_data = []
        exists_person = True

        type_data = kwargs.get('type_data', 'pessoa')
        quantity = kwargs.get('quantity', PERSON_QUANTITY)
        distiny_dir = kwargs.get('distiny_dir')
        file_name = kwargs.get('file_name')
        operation_type = kwargs.get('operation_type', 'a')


        print_log(f'GET [ {quantity} ] RANDOM PERSONs TO FILE [ RANDOM_PERSON.text ]...')

        content_persons = self.brasilian_api_generator(
            type_data=type_data, quantity=quantity
        )

        if content_persons:
            for person in content_persons:
                name_cpf = ' | '.join([person['nome'], person['cpf']])
                persons_data.append(name_cpf)


            write_content_infile(
                content_list=persons_data,
                filename=file_name,
                operation=operation_type,
                workspace_=distiny_dir,

            )

            exists_person = True
            print_log('DONE')

        else:
            exists_person = False
            print_log('NO PERSON WRITED')

        return exists_person
