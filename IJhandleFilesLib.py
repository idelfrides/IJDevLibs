#!/usr/bin/env python3
# -*- coding: utf-8 -*-



""" This module hold attributes and methods necessary to help
    build this app better."""


import glob
from datetime import datetime
import os
import pandas as pd

from .IJGeneralLib import (
    print_log, chdir_witout_log,
)

from utils.config_contants_paths import (
    FILE_OPERATION_TYPE,
    HEADER_PIPE_SEPARATOR
)


# ---------------------------------------------------------------
#                    FUNCTIONS GOES HERE
# ---------------------------------------------------------------


def convert_xlsx_to_csv_file(origin_full_file_path, destiny_real_path, result_file_name):

    xlsx_content = pd.read_excel(origin_full_file_path)

    real_result_file_name = '{}.csv'.format(result_file_name)

    xlsx_content.to_csv(destiny_real_path + real_result_file_name, sep='|')


def create_file(distiny_dir, file_name):
    print_log(f'CREATING A FILE NAMED {file_name} IN DIR {distiny_dir}')

    try:
        os.mkdir(distiny_dir)
    except Exception as excep:
        print_log('EXCEPTION: {excep}')


    chdir_witout_log(workspace=distiny_dir)

    if os.path.exists(file_name): # file existis
        print_log(f'FILE [{file_name}] ALREADY EXISTS IN DIR [ {distiny_dir} ]')

    else: # file do not existis yet

        if not len(str(file_name).split('.')) == 2:
            file_name = file_name + '.text'

        with open(file_name, 'w', encoding='utf-8') as file_obj:
            file_obj.write('INITIAL CONTENT: CREATING THIS FILE')


    chdir_witout_log()
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


    chdir_witout_log()
    print_log('DONE')

    return


def readlines_content_fromfile(distiny_dir, file_name):
    print_log(f'READING content from file {file_name}...')

    chdir_witout_log(workspace=distiny_dir)

    if not len(str(file_name).split('.')) == 2:
        file_name = file_name + '.text'


    with open(file_name, 'r', encoding='utf-8') as file_obj:
        file_content = file_obj.readlines()


    chdir_witout_log()
    print_log('DONE')

    return file_content


def read_content_fromfile(distiny_dir, file_name):
    print_log(f'READING content from file {file_name}...')

    chdir_witout_log(workspace=distiny_dir)

    if not len(str(file_name).split('.')) == 2:
        file_name = file_name + '.text'


    with open(file_name, 'r', encoding='utf-8') as file_obj:
        file_content = file_obj.read()


    print_log('DONE')
    chdir_witout_log()

    return file_content


def write_log_file(**kwarg):
    """ Informe 3 paramters with values in the order bellow.

    content='SOME CONTENT'
    distiny_dir='DESTINY DIR NAME'
    filename='YOUR FILENAME' WITHOUT '.log'
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

    chdir_witout_log()
    print_log('DONE')

    return


def join_files(full_path_files, files_names=[]):
    pass


def clean_folder(folder_name=None, keet_files=[]):
    """ Clean a folder especified on parameter folder_name.

        NOTE 1: informe the real name of the folder you want to clean up WITHOUT '/' at last of string path

    """

    print_log(f'REMOVING ALL FILES IN FOLDER --> [ {folder_name} ] ')

    chdir_witout_log(workspace=folder_name)

    for file_ in glob.glob('*', recursive=True):
        if file_ in keet_files:
            continue

        try:
            os.remove(file_)
        except Exception as error_file:
            print_log(f'EXCEPTION FILE: {error_file}')
            try:
                os.rmdir(file_)
            except Exception as error_dir:
                print_log(f'EXCEPTION DIR: {error_dir}')
                continue


    chdir_witout_log()
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


def write_output_file(**kwarg):

    workspace_ = str(kwarg['workspace'])

    if workspace_:
        chdir_witout_log(workspace=workspace_)
    else:
        chdir_witout_log(workspace='stage/OUTPUT_FILES')


    filename = kwarg['filename']
    content = str(kwarg['content'])


    with open(filename, 'a', encoding='utf-8') as file_obj:
        content += '\n'
        log_time = datetime.now()
        log_time = f'[ {str(log_time)[:19]} ] '
        real_content  = '| '.join([log_time, content])
        file_obj.write(real_content)

    chdir_witout_log()

    return



def write_content_infile(content_list, filename='RANDOM_PERSON.text', operation='a', workspace_='stage/FILES_DIR'):

    chdir_witout_log(workspace=workspace_)

    with open(filename, operation, encoding='utf-8') as file_obj:
        for content_ in content_list:
            content_ += '\n'
            file_obj.write(content_)

    chdir_witout_log()

    return


def get_random_person_from_local_file(local_dir='stage/FILES_DIR', filename='RANDOM_PERSON.text'):

    chdir_witout_log(workspace=local_dir)

    with open(filename, 'r', encoding='utf-8') as file_obj:
        cpf_content = file_obj.read()
        cpf_content = cpf_content.split('\n')

    chdir_witout_log()

    return cpf_content


def get_project_informations(filename_=None):
    """
    ### return PROJECT_ID, PROJECT_NAME

    """


    if not filename_:
        filename_ = 'project_infos.text'

    infos = read_content_fromfile(
        path_dir='stage/FILES_DIR',
        file_name=filename_
    )

    infos = infos.split('\n')
    id_ = infos[0].replace('PROJECT_ID=', '')
    name_ = infos[1].replace('PROJECT_NAME=', '')

    return id_, name_



def save_project_informations(project_id, project_name):
    file_name = 'project_infos.text'

    project_id = f'PROJECT_ID={project_id}'
    project_name = f'PROJECT_NAME={project_name}'

    content_ = [project_id, project_name]

    write_content_infile(
        content_list=content_,
        filename=file_name,
        operation=FILE_OPERATION_TYPE['write']
    )

    return