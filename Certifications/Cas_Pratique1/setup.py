
from setuptools import setup
from setuptools import find_packages

with open("requirements.txt") as f:
    content = f.readlines()
requirements = [x.strip() for x in content if "git+" not in x]

setup(
    name='project_template',
    version='0.0.1',
    install_requires= requirements,
    packages= find_packages(),
    scripts=["scripts/Cas_Pratique1"]
)
