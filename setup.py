from setuptools import find_packages, setup
from typing import List
import os

HYPEN_E_DOT = "-e ."


def get_requirements(file_path: str) -> List[str]:
    """
    Return requirements as a list of strings.
    """
    requirements = []

    # Absolute path fix (VERY important)
    abs_path = os.path.join(os.path.dirname(__file__), file_path)

    with open(abs_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    name="mlproject",
    version="0.0.1",
    author="Rahul Jakkampoodi",
    author_email="jrahul4422@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirments.txt"),  # 👈 your file name
)
