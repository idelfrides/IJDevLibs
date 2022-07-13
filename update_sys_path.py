from glob import glob
import os, sys


def setup_dev_environment():
    print('\n\n START PREPARING THE ENVIRONMENT ...\n\n')

    cwd = os.getcwd()
    cwd += '/'

    ijgu_package_stage = cwd + 'IJGeneralUsagePackage/'

    for one_module in glob('*.py', recursive=True):

        if one_module == 'update_sys_path.py':
            continue

        ijgu_package_stage += one_module

        if ijgu_package_stage not in sys.path:
            sys.path.append(ijgu_package_stage)
            print(f'\n\n CURRENT PATH SYSTEM \n\n  {sys.path}')

    return



if __name__ == '__main__':
    setup_dev_environment()
