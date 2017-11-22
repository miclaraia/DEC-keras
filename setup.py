"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the version string from the VERSION file
with open(path.join(here, 'VERSION'), 'r') as f:
    version = f.readline().strip()

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='dec_keras',
    version=version,
    description='Keras implementation for Deep Embedding Clustering (DEC)',
    long_description=long_description,
    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=[
        'numpy',
        'keras',
        'tensorflow',
        'sklearn',
        'pydot',
        'graphviz',
    ],
)
