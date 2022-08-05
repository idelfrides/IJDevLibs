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

# --------------------------------------------------------------


def setupIJDevlibs():

    print_log('START MAKING ALL SETUP . . .')

    root_proj = get_my_project_root_path()
    brgenapi = BrazilianGeneratorAPI()


    try:
        os.mkdir(f'{root_proj}/stage')
    except Exception as error:
        print_log(f'EXCEPTION: {error}')


    home_stage_path('OUTPUT_FILES', clean_ifexists=True)

    home_stage_path('FILES_DIR')


    if not os.path.exists(RANDOM_PERSON_FILE_PATH):
        if not brgenapi.brasilian_api_generator_tofile(
            type_data='pessoa'):
            return

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
