import os,glob
from setuptools import setup,find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="riboflow",
    version="1.0.0",
    author="Keshav Aditya R.P",
    author_email="keshavaditya26896@gmail.com",
    description="Classifying Putative Riboswitch Sequences",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/KeshavAdityaRP/riboflow",
    packages=['riboflow'],
    include_package_data = True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)      