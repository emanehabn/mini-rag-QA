from setuptools import find_packages, setup

from typing import List

def get_requirements()->List[str]:
    """
        Returns list of requirements
    """
    req_list:List[str] = []

    try:
        with open('requirements.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                req = line.strip()
                ## ignore empty lines and -e .

                if req and not req.startswith("-e"):
                    req_list.append(req)

    except FileNotFoundError:
        print("requirements.txt not found")
    
    return req_list

print(get_requirements())
print("++++++++++++++++++")

setup(
    name="Eman-FlipCart-Recommender",
    version="0.0.1",
    author="Eman Nasef",
    author_email="em****",
    packages=find_packages(),
    install_requires=get_requirements()

)