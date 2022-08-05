"""
Instance config file
"""


import os

DEBUG = True

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# i will config postgress

SQLALCHEMY_DATABADE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'ijdevelopmentdb.db')

SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = ''

FLASK_HOST = 'localhost'

FLASK_PORT = 7070