from setuptools import setup, find_packages
import re

def get_long_description():
    with open('README.md') as f:
        return re.sub('!\[(.*?)\]\(docs/(.*?)\)', r'![\1](https://github.com/hz-lschick/mara-db-bigquery/raw/master/docs/\2)', f.read())

setup(
    name='mara-db-bigquery',
    version='0.1.0',

    description='Extends mara-db with support for Google Big Query database',

    long_description=get_long_description(),
    long_description_content_type='text/markdown',

    url = 'https://github.com/hz-lschick/mara-db-bigquery',

    install_requires=[
        'mara-db>=4.5.0'],

    extras_require={
        'test': ['pytest', 'pytest_click'],
    },

    packages=find_packages(),

    author='Mara contributors',
    license='MIT',

    entry_points={},
    python_requires='>=3.6'
)
