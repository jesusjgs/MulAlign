# -*- coding: utf-8 -*-


from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='Classes',
    version='1.0.0',
    description='Multiple Alignment Tool',
    long_description=readme,
    author='Jesús Gómez Sola',
    author_email='jgsp64b@uma.es',
    url='https://github.com/jesusjgs/MulAlign',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
