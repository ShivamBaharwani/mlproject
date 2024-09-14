from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str) ->List[str]:
    '''
    this function will returns the list of requirements
    '''
    requirements = []
    with open(file_path,'r')as file_obj:
        requirements = file_obj.readlines()
        requirements=[req.replace('\n',"") for req in requirements]
        

    return requirements


setup(
    name = 'mlproject',
    version = '0.0.1',
    author = 'Shivam',
    author_email = 'baharwanishivam@gmail.com',
    packages = find_packages(),
    nstall_requires = get_requirements('requirements.txt'),
)