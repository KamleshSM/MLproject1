from setuptools import find_packages,setup
from typing import List

Hyphen_e_dot = "-e ."
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return list of requriements
    '''
    requriements = []
    with open(file_path) as file_obj:
        requriements = file_obj.readlines()
        requriements = [req.replace("\n","") for req in requriements]
        
        if Hyphen_e_dot in requriements:
            requriements.remove(Hyphen_e_dot)

    return requriements





setup(
    name = "mlproject1",
    version = "0.0.1",
    author = "Kamlesh",
    author_email = "kamleshsmahajan11235@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements("requirements.txt")
  
)