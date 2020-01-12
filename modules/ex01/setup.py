from setuptools import setup, find_packages

setup(
    name='mathematica',
    version='1.0.0',
    description='Math utils.',
    packages=find_packages(exclude=['tests']),
)
