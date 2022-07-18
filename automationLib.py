
from time import time
import pyautogui
import pandas as pd
from playwright.sync_api import sync_playwright

from selenium import webdriver                   # controle o browser
from selenium.webdriver.common.keys import Keys  # cpntrola o teclado do seu PC
from selenium.webdriver.common.by import By

from .IJGeneralLib import (
    convert_minutes_to_second, print_log
)


def bot_convert_file():

    """
        IN construction yet
        TODO: FINISH THIS FUNCTION

        NOTE 1 : do not user this function
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
