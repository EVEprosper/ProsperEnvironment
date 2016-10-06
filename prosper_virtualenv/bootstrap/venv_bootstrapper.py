#!/usr/bin/env python3
'''venv_bootstrapper.py: uses virtualenv bootstrap functionality
    Sets up basic requirements for any Prosper project
    https://virtualenv.pypa.io/en/stable/reference/?highlight=bootstrap#creating-your-own-bootstrap-scripts'''

from os import path
import sys
import configparser
from configparser import ExtendedInterpolation

import virtualenv

CURRENT_DIR = path.abspath(path.dirname(__file__))
CONFIG_PATH = path.join(CURRENT_DIR, 'bootstrap.cfg')

def get_config(config_file = CONFIG_PATH):
    '''parse config file for global vars'''
    pass

def main():
    '''runs create_boostrap_script functionality and spits out new virtualenv script'''
    pass

if __name__ == '__main__':
    main()
