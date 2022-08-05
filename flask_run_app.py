#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Pyton importatinons
import os
from random import randint
import time

from flask_app import __app__, render_template, request

# external lib importation
from IJGeneralLib import (
    clean_diretory, build_line,
    convert_minutes_to_second,
    make_sound, print_log,
    show_info,
    make_reponse,
)

from utils.config_contants_paths import (
    APP_INFO
)

from setup_app import setupIJDevlibs

#-------------------------------------------------------------------------
#                  RUN APP FUNCTION BEGIN HERE
#-------------------------------------------------------------------------


@__app__.route('/home')
@__app__.route('/inicio')
@__app__.route('/index')
@__app__.route('/')
def hello():

    print(APP_INFO)

    return make_reponse(endpoint='home or inicio or index or /')


@__app__.route('/ijdevlibs_setup')
@__app__.route('/ijdevlibs_setup/<project_id>/<project_name>')
def setup_starkbankapp(project_id=None, project_name=None):

    setupIJDevlibs()

    return make_reponse(endpoint='setupIJDevlibs')



# -----------------------------------------------------------------------------


if __name__ == '__main__':

    __app__.run(
        __app__.config['FLASK_HOST'], port=__app__.config['FLASK_PORT']
    )
