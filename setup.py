from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.readlines()

setup(
    name='search_engines',
    version='0.5',
    description='Search Engines Scraper CSE',
    author='Tasos M. Adamopoulos, modified by Craig S. Echt',
    license='MIT, GNU',
    packages=find_packages(),
    install_requires=requirements
)
