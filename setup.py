#!/usr/bin/env python

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="DDLJ",
    version="0.0.15",
    author="Arghadeep Chaudhury,Siddhartha Bhattacharya",
    author_email="siddhbhatt@gmail.com,arghadeep.chaudhury@gmail.com",
    description="JSON Utils for generating DDL from JSON Schema",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/deepstartup/jsonutils",
    packages=find_packages(),
    install_requires=['pandas', 'flatten_json'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)