#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# Copyright 2018, Nigel Small
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from os.path import dirname, join as path_join
try:
    from setuptools import setup, Extension
except ImportError:
    from distutils.core import setup, Extension

from _blueprint.meta import package, version


install_requires = [
]
classifiers = [
    "Intended Audience :: Developers",
    "License :: OSI Approved :: Apache Software License",
    "Operating System :: OS Independent",
    "Topic :: Software Development :: Libraries",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3.4",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
]
packages = [
    package,
]
setup_args = {
    "name": package,
    "version": version,
    "description": "TODO",
    "license": "Apache License, Version 2.0",
    "long_description": open(path_join(dirname(__file__), "README.rst")).read(),
    "author": "Nigel Small",
    "author_email": "technige@nige.tech",
    "url": "https://_blueprint.readthedocs.io",
    "install_requires": install_requires,
    "classifiers": classifiers,
    "packages": packages,
}

setup(**setup_args)
