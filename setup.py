from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = '-e .'


def get_requirements(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
      
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)


    return requirements
        


setup(
    name="Store Sales Prediction",
    version="0.0.1",
    author="Revan",
    author_email="brevankumar@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
      )




#febev





