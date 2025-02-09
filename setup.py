#!/bin/env python
import os

from setuptools import setup


def find_xdg_data_files(syspath, relativepath, pkgname, data_files=[]):
    for (dirname, _, filenames) in os.walk(relativepath):
        if filenames:
            syspath = syspath.format(pkgname=pkgname)

            subpath = dirname.split(relativepath)[1]
            if subpath.startswith("/"):
                subpath = subpath[1:]

            files = [os.path.join(dirname, f) for f in filenames]

            data_files.append((os.path.join(syspath, subpath), files))

    return data_files


def find_data_files(data_map, pkgname):
    data_files = []

    for (syspath, relativepath) in data_map:
        find_xdg_data_files(syspath, relativepath, pkgname, data_files)

    return data_files


DATA_FILES = [
    ("share/{pkgname}/plugins", "data/plugins"),
]


setup(
    author="Juan Manuel Schillaci",
    author_email="jmschillaci@gmail.com",
    description="Focusyn plugin that shows screen notifications.",
    include_package_data=True,
    keywords="pomodoro,timer",
    license="GPL-3",
    long_description=open("README.md").read(),
    name="focusyn-notify-plugin",
    data_files=find_data_files(DATA_FILES, "focusyn"),
    url="https://github.com/skajms/focusyn-notify-plugin",
    version="0.1.0",
    zip_safe=False,
)
