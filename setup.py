import sys

from setuptools import setup, find_packages

setup(
    name='vt',
    version='1.0.0',
    description='VirusTotal Full API',
    packages=find_packages(),
    url='https://github.com/doomedraven/VirusTotalApi',
    license='GPLv3',
    author = 'Andriy Brukhovetskyy - DoomedRaven',
    author_email='Twitter -> @D00m3dR4v3n',
    entry_points={
        'console_scripts': [
            'vt = vt.__main__:main',
        ],
    },
    install_requires=[
        "requests >= 2.1.0",
        "texttable >= 0.8.1",
        "python-dateutil >= 1.5"
    ],
)
