from setuptools import find_packages
from setuptools import setup

setup(
    name='ngc_interfaces',
    version='0.0.0',
    packages=find_packages(
        include=('ngc_interfaces', 'ngc_interfaces.*')),
)
