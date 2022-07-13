#!/src/bin/env python3
# encoding: utf-8


""" This module hold attributes and methods necessary to help
    build this app better."""


import glob
import os, shutil
from datetime import datetime
import pandas as pd

from .ijfunctions import (
    print_log, chdir_witout_log,
    chdir_with_log
)

from .hold_constants_paths import (
    HEADER_PIPE_SEPARATOR
)


# ---------------------------------------------------------------
#                    FUNCTIONS GOES HERE
# ---------------------------------------------------------------


def convert_xlsx_to_csv_file(origin_full_file_path, destiny_real_path, result_file_name):

    xlsx_content = pd.read_excel(origin_full_file_path)

    real_result_file_name = '{}.csv'.format(result_file_name)

    xlsx_content.to_csv(destiny_real_path + real_result_file_name, sep='|')


def write_content_infile(content_list, distiny_dir, file_name, operation_type='w'):
    print_log(f'WRITTING [ {len(content_list)} ] CONTENT TO FILE {file_name}...')

    chdir_witout_log()
    # chdir_witout_log(distiny_dir=distiny_dir)

    try:
        os.mkdir(distiny_dir)
    except Exception as error:
        print_log(f'EXCEPTION -> {error}')

    chdir_witout_log(workspace=distiny_dir)

    if not len(str(file_name).split('.')) == 2:
        file_name = file_name + '.text'

    with open(file_name, operation_type, encoding='utf-8') as file_obj:
        for content_ in content_list:
            cpf_with_end_line = str(content_) + '\n'
            file_obj.write(cpf_with_end_line)

    print_log('DONE')

    return


def create_file(distiny_dir, file_name):
    print_log(f'CREATING A FILE NAMED {file_name} IN DIR {distiny_dir}')

    try:
        os.mkdir(distiny_dir)
    except Exception as excep:
        print_log('EXCEPTION: {excep}')


    if os.path.exists(file_name): # file existis
        print_log(f'FILE [{file_name}] ALREADY EXISTS IN DIR [ {distiny_dir} ]')

        print_log('DONE')

    else: # file do not existis yet

        if not len(str(file_name).split('.')) == 2:
            file_name = file_name + '.text'

        with open(file_name, 'w', encoding='utf-8') as file_obj:
            file_obj.write('')

        print_log('DONE')

    return



def create_diretory(dirname, workspace_=None):
    print_log(f'CREATING A DIR NAMED --> [{dirname}] IN WORKSPACE [{workspace_}]')

    if not workspace_:    # mkdir in current workspace
        chdir_witout_log()
    else:
        chdir_witout_log(workspace=workspace_)


    try:
        os.mkdir(dirname)
    except Exception as excep:
        print_log('EXCEPTION: {excep}')
        print_log(f'FILE [{dirname}] ALREADY EXISTS IN WORKSPACE [ {workspace_} ]')

    print_log('DONE')

    return


def read_content_fromfile(distiny_dir, file_name):
    print_log(f'READING content from file {file_name}...')

    chdir_witout_log()

    try:
        os.mkdir(distiny_dir)
    except Exception as excep:
        print_log('EXCEPTION: {excep}')

    chdir_witout_log(workspace=distiny_dir)

    if not len(str(file_name).split('.')) == 2:
        file_name = file_name + '.text'


    with open(file_name, 'r', encoding='utf-8') as file_obj:
        file_content = file_obj.readlines()

    print_log('DONE')

    return file_content


def write_log_file(**kwarg):
    """ Informe 3 paramters with values in the order bellow.

    content='SOME CONTENT'
    distiny_dir='DESTINY DIR NAME'
    filename='YOUR FILENAME'
    """

    chdir_witout_log()

    distiny_dir = kwarg['distiny_dir']

    try:
        os.mkdir(distiny_dir)
    except Exception as excep:
        print_log(f'EXCEPTION: {excep}')


    filename = kwarg['filename']
    filename = filename + '.log'
    content = str(kwarg['content'])

    print_log(f'WRITTING [ {len(content)} ] CONTENT TO FILE {filename}...')

    chdir_witout_log(workspace=distiny_dir)

    with open(filename, 'a', encoding='utf-8') as file_obj:
        content += '\n'
        log_time = datetime.now()
        log_time = f'[ {str(log_time)[:19]} ] '
        real_content  = '| '.join([log_time, content])
        file_obj.write(real_content)

    print_log('DONE')

    return


def join_files(full_path_files, files_names=[]):
    pass


def clean_folder(folder_path, keet_files=[]):
    """ Clean a folder especified on parameter folder_path.

        NOTE 1: informe the real full path of the folder you want to clean up WITHOUT '/' at last of string path

    """

    folder_name = str(folder_path).split('/')[-1]

    print_log(f'REMOVING ALL FILES IN FOLDER --> [ {folder_name} ] ')

    chdir_witout_log(workspace=folder_path)

    for file_ in glob.glob('*', recursive=True):
        if file_ in keet_files:
            continue

        try:
            os.remove(file_)
        except Exception as error_file:
            print_log(f'EXCEPTION FILE: {error_file}')
            try:
                os.removedirs(file_)
            except Exception as error_dir:
                print_log(f'EXCEPTION DIR: {error_dir}')
                continue


    print_log('DONE')
    return


def prepare_convert_files_to_csv(filetype=None, full_file_path=None, destiny_dir_path=None, result_file_name=None):

    if not result_file_name:   # use the same file name
        result_file_name = str(full_file_path).split('/')[-1]
        result_file_name = str(result_file_name).split('.')[0]

    if not destiny_dir_path:   # use the same folder
        destiny_dir_path_list = str(full_file_path).split('/')
        len_list = len(destiny_dir_path_list)
        _ = destiny_dir_path_list.pop(len_list - 1)

        while '' in destiny_dir_path_list:
           destiny_dir_path_list.remove('')

        destiny_dir_path = '/'.join(destiny_dir_path_list)

    if filetype == 'xlsx':

        convert_xlsx_to_csv_file(
            full_file_path, destiny_dir_path, result_file_name
        )

    elif filetype == 'json':
        # TODO: Create a logic for this operation
        pass
    else:
        pass


    return



def convert_xlsx_to_csv_file(origin_full_file_path, destiny_real_path, result_file_name):

    xlsx_content = pd.read_excel(origin_full_file_path)

    destiny_real_path += '/'

    xlsx_content.to_csv(
        destiny_real_path + result_file_name, sep=HEADER_PIPE_SEPARATOR
    )

    return
