from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
#returns a list of requirements for the project
def get_requirements(file_path: str)->List[str]:
    with open('requirements.txt') as f:
        requirements=f.read().splitlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
            
    return requirements

    
setup(
   name='mlproject',
   version='0.0.1',
   author='Arkajyoti Naskar',
   author_email='arkajyoti2708@gmail.com',
   packages=find_packages(),
   install_requires=get_requirements('requirements.txt')
)
