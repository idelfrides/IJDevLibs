
#!/usr/bin/env python3
# -*- coding: utf-8 -*-



import errno
import glob
from random import randint
import time
from datetime import datetime
import wget
import requests
import os, shutil

from utils.config_contants_paths import (
    IJDEVLIBS_SPLIT,
    MIN_LIMIT,
    MAX_LIMIT,
    IJDEVLIBS
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


def chdir_witout_log(workspace=None, return_cwdir='No'):
    """ ready to use """

    project_root_dir = os.path.dirname(os.path.abspath(__file__))

    project_root_dir = project_root_dir.split(IJDEVLIBS_SPLIT)[0]
    os.chdir(project_root_dir)

    if not workspace:
        pass
    else:
        os.chdir(workspace)

    if return_cwdir.upper() == 'YES':
        print_log('DONE')
        return os.getcwd()

    return


def chdir_with_log(workspace=None, return_cwdir='No'):
    project_root_dir = os.path.dirname(os.path.abspath(__file__))

    project_root_dir = project_root_dir.split(IJDEVLIBS_SPLIT)[0]
    os.chdir(project_root_dir)

    if not workspace:
        print_log(f'CHANGING WORKSPACE TO DIR --> [ {project_root_dir} ] ...')
    else:
        print_log(f'CHANGING WORKSPACE TO DIR --> [ {workspace} ] ...')
        os.chdir(workspace)

    if return_cwdir.upper() == 'YES':
        print_log(' CHANGING WORKSPACE DONE')
        return os.getcwd()

    print_log(' CHANGING WORKSPACE DONE')

    return


def show_warning(**kwargs):

    if kwargs['type_'] == 'warning':

        warning_info = f"""
        warning--warning--warning--warning--warning--warning--warning--warning-

                                    WARNING
        -----------------------------------------------------------------------

                WARNING TYPE/NAME: [ {kwargs['type_name']} ]
                SMALL DESCRIPTION --> {kwargs['desc_']}
                {kwargs['user_key']} --> {kwargs['user_key_value']}

        warning--warning--warning--warning--warning--warning--warning--warning-
        """

    print(warning_info)
    make_sound(frequency=150)
    time.sleep(20)

    return


def delete_file(dir_name, file_name):

    print_log(f'REMOVING FILE [{file_name}] IN DIR --> [ {dir_name} ] ')

    if not dir_name or not file_name:
        show_warning(
            type_='warning',
            type_name='ARGUMENTS EMPTY',
            desc_= 'parameter [dir_name, file_name] ARE REQUIRED',
            user_key='BE A MAN',
            user_key_value='FILL THOSE PARAMETER WITH VALID VALUES'
        )

        return

    chdir_witout_log(workspace=dir_name)

    try:
        os.remove(file_name)
    except Exception as error_file:
        print_log(f'EXCEPTION FILE: {error_file}')

    chdir_witout_log()    # back to root project
    print_log('DONE')

    return


def delete_dir(workspace_name=None, dir_name_list=[]):
    """ Pass only folder structure without last backslash '/'.

    Exemple:
        [1] DIR_1/DIR_2
        [2] DIR_1/DIR_2/DIR_3

    """

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

    chdir_witout_log()   # back to root project
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


def make_reponse(endpoint):

    ij_jsonify = {
        'state': 'SUCCESS',
        'status': 200,
        'function': '{}'.format(str(endpoint))
    }

    return ij_jsonify


def complete_make_response(**kwargs):

    total_minutes = kwargs['total_minutes']
    total_seconds = kwargs['total_seconds']
    user_key = kwargs.get('user_key', '')
    user_key_value = kwargs.get('user_key_value', '')

    if (not user_key_value and user_key) or (not user_key and user_key_value):
        build_line('bad-', 100)
        print_log('\n\n WARNING: \n PARAMETERS "user_key" and  "user_key_value" WORKS TOGETHER. SO, YOU NEED TO SET ALL OF THEM.')
        build_line('bad-', 100)
        make_sound()
        return

    # if not user_key and user_key_value:
    #     build_line('bad-', 100)
    #     print_log('\n\n WARNING: \n IF YOU SET "user_key" PARAMETER YOU NEED TO SET "user_key_value" TOO.')
    #     build_line('bad-', 100)
    #     return


    build_line('#', 100)

    ij_jsonify = ("""
    {
        'state': 'SUCCESS',
        'status': 200,
        '%s': '%s',
        'total time': '%.0f minute(s) e %.0f miliseconds'
    }""" % (str(user_key).upper(), user_key_value, int(total_minutes), int(total_seconds)), 200)

    print('{}'.format(ij_jsonify[0]))

    build_line('#', 100)

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


def copy_or_move_files(file_name, operation, originPath, destinyPath):

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
    """## Clean a folder especified in parameter 'folder_path'.

        #### NOTE 1: informe the real name of the folder you want to clean up WITHOUT '/' at last of string path

    """

    if not folder_path:
        print_log('"folder_path" parameter is EMPTY')
        return

    folder_name = str(folder_path).split('/')[-1]

    print_log(f'REMOVING ALL FILES IN FOLDER --> [ {folder_name} ] ... ')

    chdir_witout_log(workspace=folder_path)

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


    chdir_witout_log()    # back to root project
    print_log('DONE')
    return


def show_info(**kwargs):

    if kwargs['type_'] == 'app_info':

        info = f"""
        ------------------------------------------------------------
                APP NAME: [ {kwargs['app_name']} ]
                SMALL DESCRIPTION: {kwargs['desc_']}
                APP VERSION: {kwargs['version_']}
                {kwargs['user_key']}: {kwargs['user_key_value']}
        -------------------------------------------------------------
        """

    if kwargs['type_'] == 'round_info':

        info = f"""
        ------------------------------------------------------------
                GAME ROUND : [ {kwargs['value_']} ]
                PLAYER PROFILE: {kwargs['player']}
                PLAYER BALANCE: {kwargs['balance']}
        ------------------------------------------------------------
        """

    if kwargs['type_'] == 'game_info':

        info = f"""
        ------------------------------------------------------------
                SIMULATION/PARTIDA --> [ {kwargs['value_']} ]
                GAME ROUND --> [ {kwargs['value_round']} ]
                PLAYER PROFILE --> {kwargs['player']}
                PLAYER BALANCE --> {kwargs['balance']}
        ------------------------------------------------------------
        """

    if kwargs['type_'] == 'simulation_info':

        info = f"""
        ----------------------------------------------------------

                GAME SIMULATION/PARTIDA : [ {kwargs['value_']} ]

        ----------------------------------------------------------
        """

    print(info)

    return


def custom_show_info(some_code, person):
    info = """
    ---------------------------------------------------------------------------
        CREATING INVOICE FOR --> [ {} ]
        INVOICE ORDER --> [ {} ]
    ---------------------------------------------------------------------------
    """.format(person, some_code)

    print(info)
    time.sleep(3)

    return


def define_random_number(min_limit=MIN_LIMIT, max_limit=MAX_LIMIT):
    """
    # define_random_number function
    #### DEFAULT VALUES
    ####   --> min_limt = 1 | max_limit = 100

    """

    print_log(f'RANDOMIC DEFINING ORDER/NUMBER ...')

    random_number = randint(min_limit, max_limit)

    print_log(f'GENERATED NUMBER IS --> {random_number}')

    return random_number


def write_list_content_infile(content_list, distiny_dir, file_name, operation_type='w'):
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

    chdir_witout_log()
    print_log('DONE')

    return


def home_path(destiny_dir):
    """
    Defines path based on OS
    """

    # root_project = chdir_witout_log(return_cwdir='YES')
    root_project = os.getcwd()


    # Emulate path for current project
    return_path = os.path.join(str(root_project), destiny_dir, '')

    # Create if not exists
    try:
        os.makedirs(return_path)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(return_path):
            pass
        else:
            raise

    return return_path


def home_stage_path(destiny_dir, clean_ifexists=False):
    """
    Defines path based on OS
    """

    # root_project = chdir_witout_log(return_cwdir='YES')
    # root_project = os.getcwd()
    root_project = get_my_project_root_path()

    # Emulate path for current project
    return_path = os.path.join(str(root_project), 'stage', destiny_dir, '')


    if clean_ifexists:  # clean ij exists
        try:
            os.makedirs(return_path)
        except OSError as exc:
            if exc.errno == errno.EEXIST and os.path.isdir(return_path):
                clean_diretory(folder_path=f'stage/{destiny_dir}')
            else:
                raise

    else:
        # Create if not exists
        try:
            os.makedirs(return_path)
        except OSError as exc:
            if exc.errno == errno.EEXIST and os.path.isdir(return_path):
                pass
            else:
                raise


    return return_path



def get_my_project_root_path():
    """# This function will return your root dir """

    project_root_dir = os.path.dirname(os.path.abspath(__file__))

    project_root_dir = project_root_dir.split(IJDEVLIBS_SPLIT)[0]

    return project_root_dir
