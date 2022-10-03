from setuptools import setup, find_packages
from typing import List

PROJECT_NAME="Premium-Predictor"
VERSION="0.0.1"
AUTHOR="Anuj K."
DESCRIPTION="This is an app for predicting insurance premium"
REQUIREMENT_FILE_NAME="requirements.txt"

def get_requirements_list()->List[str]:
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
        requirement_list = [requirement_name.replace("\n", "") for requirement_name in requirement_list]
        if '-e .' in requirement_list:
            requirement_list.remove('-e .')
        return requirement_list


setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    package=find_packages(),
    install_requires=get_requirements_list()
)