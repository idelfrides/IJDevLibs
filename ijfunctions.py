
# !/src/bin/env python3
# encoding: utf-8

import glob
import pstats
import time
from datetime import datetime
import wget
import requests
import os, shutil
import pyautogui
import pandas as pd
from playwright.sync_api import sync_playwright

from selenium import webdriver                   # controle o browser
from selenium.webdriver.common.keys import Keys  # cpntrola o teclado do seu PC
from selenium.webdriver.common.by import By

from .hold_constants_paths import (
    IJGU_PACKAGE
)


# ---------------------------------------------------------------
#                    FUNCTIONS GOES HERE
# ---------------------------------------------------------------


def ij_smart_menu(list_of_menu_options):

    while True:
        print("""
        -----------------------------------------
                    MENU OF CHOICES
        -----------------------------------------
        """)

        options_quantity = len(list_of_menu_options)

        for index, option in enumerate(list_of_menu_options, start=1):
            print(f'\t {index} --> {str(option).upper()}')

        options_quantity += 1

        print(f'\t {options_quantity} --> ADD A NEW OPTION')
        if options_quantity > 1:
            print(f'\t {-1} --> REMOVE ALL OPTIONS')

        print('\t 0 --> QUIT APP\n ')

        try:
            response_ = int(input('  INFORME UMA OPCAO:   '))
        except Exception as err:
            make_sound(frequency=300)
            build_line('-', 80)
            print(f'\t WARNING: INVALID OPTION')
            build_line('-', 80)
            response_ = 'QUIT'

        if response_ == -1 or response_ in range(options_quantity + 1):
            break

    return response_


def convert_minutes_to_second(minutes):
    return 60 * minutes


def convert_minutes_to_hour(minutes):
    return minutes / 60


def convert_seconds_to_minutes(seconds):
    return seconds / 60


def convert_hour_to_minute(hours):
    return hours * 60


def convert_hour_to_second(hours):
    total_minutes = convert_hour_to_minute(hours)
    seconds = convert_minutes_to_second(total_minutes)
    return seconds


def make_sound(frequency=300, duration=1):
    os.system('play -nq -t alsa synth {} sine {}'.format(duration, frequency))


def build_line(shape, length_line):

    print('\n')
    print('{}'.format(shape) * length_line)
    print('\n')

    return


def chdir_with_log(workspace=None, return_cwdir='No'):
    project_root_dir = os.path.dirname(os.path.abspath(__file__))

    project_root_dir = project_root_dir.split('/IJGeneralUsagePackage')[0]
    os.chdir(project_root_dir)

    if not workspace:
        print_log(f'CHANGING WORKSPACE TO DIR --> [ {project_root_dir} ] ...')
    else:
        print_log(f'CHANGING WORKSPACE TO DIR --> [ {workspace} ] ...')
        os.chdir(workspace)

    if return_cwdir.upper() == 'YES':
        return os.getcwd()

    print_log(' CHANGING WORKSPACE DONE')

    return


def chdir_witout_log(workspace=None, return_cwdir='No'):
    """ ready to use """

    project_root_dir = os.path.dirname(os.path.abspath(__file__))

    project_root_dir = project_root_dir.split('/IJGeneralUsagePackage')[0]
    os.chdir(project_root_dir)

    if not workspace:
        pass
    else:
        os.chdir(workspace)

    if return_cwdir.upper() == 'YES':
        print_log('DONE')
        return os.getcwd()

    print_log('DONE')

    return


def delete_file(dir_name, file_name):

    print_log(f'REMOVING FILE [{file_name}] IN DIR --> [ {dir_name} ] ')

    chdir_witout_log(workspace=dir_name)

    try:
        os.remove(file_name)
    except Exception as error_file:
        print_log(f'EXCEPTION FILE: {error_file}')

    print_log('DONE')

    return



def delete_dir(workspace_name=None, dir_name_list=[]):

    cwd = chdir_witout_log(workspace=workspace_name, return_cwdir='yes')
    workspace_name = cwd.split('/')[-1]

    for dir_name in dir_name_list:

        print_log(f'REMOVING DIR {dir_name} IN WORKSPACE [{workspace_name}] ')

        dir_path = cwd + '/' + dir_name

        if not dir_name in glob.glob('*', recursive=True):
            continue

        try:
            os.rmdir(dir_name)
        except Exception as error_dir:
            print_log(f'EXCEPTION DIR : {error_dir}')
            clean_diretory(dir_path)
            chdir_witout_log()
            os.rmdir(dir_name)

        print_log('DONE')

    return



def copy_libs(originDir=None, destinyDir=None):

    # TODO: CORRECT THIS FUNCTIN

    print_log('START COPING [ libs.py ]')

    origin_path = os.getcwd()

    distiny_path = os.getcwd()

    shutil.copy(origin_path, distiny_path)

    print_log('DONE')

    return


def print_log(content):

    log_time = datetime.now()
    log_time = f'[ {str(log_time)[:19]} ] '
    real_content = '| '.join([log_time, str(content)])

    print(f'\n{real_content}')

    return


def make_response(total_minutes, total_seconds, source_data):

    build_line('*', 80)

    ij_jsonify = ("""
    {
        'state': 'SUCCESS',
        'status': 200,
        'source data': '%s',
        'total time': '%.0f minute(s) e %.0f miliseconds'
    }""" % (str(source_data).upper(), int(total_minutes), int(total_seconds)), 200)

    print('{}'.format(ij_jsonify[0]))

    build_line('*', 80)

    return


def download_images_from_server(url_image_list, save_image_dir, wget_lib=None):

    current_workspace = chdir_witout_log(return_cwdir='yes')

    current_workspace += '/'

    products_images_path = current_workspace + save_image_dir

    image_list_lenght = len(url_image_list)

    for index_ in range(image_list_lenght):

        url_image = url_image_list[index_]

        url_image = str(url_image)

        image_name = url_image.split('/')[-1]

        if not wget_lib:

            try:
                response_ = requests.get(url_image, stream=True)

                if response_.status_code == 200:
                    response_.raw.decode_content = True

                    with open(image_name, 'wb') as f:
                        shutil.copyfileobj(response_.raw, f)

                    print_log(f'IMAGE SUCESSFULLY DOWNLOADED: [ {image_name} ]')
                else:
                    print_log('SORRY!!! IMAGE CAN NOT BE RETRIVED')
                    continue
            except Exception as error:
                print_log(f'EXCEPTION OPCCURRED:  {error}')
                continue

        else:

            response_ = wget.download(url_image)
            print_log(f'IMAGE SUCESSFULLY DOWNLOADED: [ {image_name} ]')


        copy_or_move_files(
            file_name=image_name,
            operation='move',
            originPath=current_workspace,
            destinyPath=products_images_path
        )

    return



def copy_or_move_files(file_name='', operation='', originPath='', destinyPath=''):

    """ Make COPY or MOVE a folder especified on parameter destinyPath.

        NOTE 1: informe the real full path of the folder you want to clean up WITHOUT '/' at last of string path

    """

    destiny_folder_name = destinyPath

    destiny_folder_name = destiny_folder_name.split('/')[-1]
    originPath += file_name

    if operation == 'copy':

        print_log(f'COPING FILE [{file_name}] TO [ {destiny_folder_name} ]')

        try:
            shutil.copy(originPath, destinyPath)
        except Exception as error:
            print_log(f'EXCEPTION : {error}')
    elif operation == 'move':

        print_log(f'MOVING FILE [{file_name}] TO [ {destiny_folder_name} ]')

        try:
            shutil.move(originPath, destinyPath)
        except Exception as error:
            print_log(f'EXCEPTION : {error}')
    else:
        pass

    print_log('DONE')

    return


def clean_diretory(folder_path, keet_files=[]):
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



class HoldSomeThing:

    def __init__(self, some_obj):
        self.__some_sent = some_obj

    # Getter
    def get_some_sent(self):
        return self.__some_sent

    # Setter
    def set_some_sent(self, something):
        self.__some_sent = something



def bot_convert_file():

    """
        IN construction yet
        TODO: FINISH THIS FUNCTION
    """

    XPATH_LOAD_FILE = '//*[@id="filebutton"]'
    XPATH_CONVERT_FILE = '//*[@id="convertbutton"]'

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        # browser = p.firefox.launch(headless=False)
        page = browser.new_page()

        page.goto('https://cdkm.com/pt/xml-to-csv')
        page.click(XPATH_LOAD_FILE)
        time.sleep(10)

        # import pdb; pdb.set_trace()

        # click on outros locais
        pyautogui.click(x=997, y=1021)
        time.sleep(5)

        # import pdb; pdb.set_trace()

        posi = pyautogui.position()
        print_log(posi)
        # pyautogui.click(x=1135, y=1022)

        posi = pyautogui.position()
        print_log(posi)

        # pyautogui.__loader__()
        # pyautogui.__file__()
        # pyautogui.locate()

        # click in DATA
        pyautogui.click(x=1180, y=500)
        time.sleep(5)

        # click on PROFISSIONAL folder
        pyautogui.click(x=1180, y=500, clicks=2)
        time.sleep(5)

        # click on VALERIA_FERREIRA_LIMA folder  | 2X
        pyautogui.click(x=1180, y=500, clicks=2)
        time.sleep(5)

        # click on COMERCIALFERREIRALIMA folder | 2x
        pyautogui.click(x=1180, y=500, clicks=2)
        time.sleep(5)

        # click on 'produtos_pr_csv' file | 1x
        pyautogui.click(x=1180, y=500, clicks=2)
        time.sleep(5)

        # import pdb; pdb.set_trace()

        posi = pyautogui.position()

        print_log(posi)

        # press to make converting
        page.click(XPATH_CONVERT_FILE)
        waitting_converting = convert_minutes_to_second(7)
        time.sleep(waitting_converting)

        # download result file
        page.click('x')
        waitting_download = convert_minutes_to_second(7)
        time.sleep(waitting_download)

        browser.close()

        time.sleep(30)

        print_log('CONVERT FILE TO CSV DONE... \n [STATUS: SUCCESS]')

    return
