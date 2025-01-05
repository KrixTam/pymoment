# coding: utf-8

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pymoment",
    version="0.1.0",
    packages=['moment'],
    author="Krix Tam",
    author_email="krix.tam@qq.com",
    description='The python version of "moment" which is made with reference to "moment.js"',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/KrixTam/pymoment",
    project_urls={
        "Bug Tracker": "https://github.com/KrixTam/pymoment/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    py_modules=["moment"],
    python_requires=">=3.6",
)
