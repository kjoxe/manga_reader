import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "manga_reader",
    version = "0.1",
    author = "kjoxe",
    description = ("Very minimal raw manga reader for my personal use."),
    license = "GPLv2",
    packages=['manga_reader'],
    install_requires=['PyQt5>=5.0'],
    entry_points="""
    [console_scripts]
    manga_reader = manga_reader.__main__:main
    """,
)
