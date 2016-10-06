'''wheel setup for Prosper development environment'''

from os import path, listdir
from setuptools import setup, find_packages

HERE = path.abspath(path.dirname(__file__))

def include_all_subfiles(path_included):
    '''for data_files {path_included}/*'''
    local_path = path.join(HERE, path_included)
    file_list = []

    for file in listdir(local_path):
        file_list.append(path_included + '/' + file)

    return file_list

def hack_find_packages(include_str):
    '''setuptools.find_packages({include_str}) does not work.  Adjust pathing'''
    new_list = [include_str]
    for element in find_packages(include_str):
        new_list.append(include_str + '.' + element)

    return new_list

setup(
    name='prosper_virtualenv',
    version='0.0.0',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3.5'
    ],
    keywords='prosper eveonline api environment',
    packages=find_packages(),
    data_files={
        ('docs', include_all_subfiles('docs')),
        ('scripts', include_all_subfiles('scripts'))
    },
    package_data={
        'bootstrap':'bootstrap.cfg'
    },
    install_requires=[

    ],
    dependency_links=[

    ]
)
