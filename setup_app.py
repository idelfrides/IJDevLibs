#!/usr/bin/env python3
# -*- coding:utf-8 -*-


import os
import time

from IJGeneralLib import (
    clean_diretory,
    get_my_project_root_path,
    print_log,
    home_stage_path
)

from utils.config_contants_paths import (
    PERSON_QUANTITY,
    RANDOM_PERSON_FILE_PATH,
)

from api_libs.brasilian_generator import (
    BrazilianGeneratorAPI
)


from api_libs.ngrok_api_lib import (
    NgrokAPI,

)


# ---------------------------------------------------------------


def setupIJDevlibs():

    print_log('START MAKING ALL SETUP . . .')

    root_proj = get_my_project_root_path()
    brgenapi = BrazilianGeneratorAPI()


    try:
        os.mkdir(f'{root_proj}/stage')
    except Exception as error:
        print_log(f'EXCEPTION: {error}')


    home_stage_path(destiny_dir='OUTPUT_FILES', clean_ifexists=True)

    home_stage_path(destiny_dir='FILES_DIR')

    random_person_path = f'{root_proj}/{RANDOM_PERSON_FILE_PATH}'


    if not os.path.exists(random_person_path):
        if not brgenapi.brasilian_api_generator_tofile(
            type_data='pessoa'):
            return
    else:
        print_log('FILE [ {} ] ALREADY EXISTS.'.format(RANDOM_PERSON_FILE_PATH.split('/')[2]))


    # create_user_webhook()

    print_log('SET UP DONE')

    return


def create_user_webhook():

    ngrok = NgrokAPI()

    public_url = ngrok.get_ngrok_entity(endpoint='tunnels')

    public_url = '/'.join([public_url, 'starkbank_webhook'])

    return


if __name__ == '__main__':
    setupIJDevlibs()
