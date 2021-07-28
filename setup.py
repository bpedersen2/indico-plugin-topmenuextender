# This file is part of the CERN Indico plugins.
# Copyright (C) 2014 - 2018 CERN
#
# The CERN Indico plugins are free software; you can redistribute
# them and/or modify them under the terms of the MIT License; see
# the LICENSE file for more details.

from __future__ import unicode_literals

from setuptools import find_packages, setup


setup(
    name='indico-plugin-topmenuextender',
    license='MIT',
    author='MLZ indico team',
    author_email='bjoern.pedersen@frm2.tum.de',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    use_scm_version={"write_to":"indico_topmenu_extender/version.py",
                     "local_scheme":"node-and-timestamp"},
    setup_requires = ["setuptools>=39", "setuptools_scm[toml]>=3.4"],
    install_requires=[
        'indico>=3'
    ],
    entry_points={
        'indico.plugins': {'topmenu_extender=indico_topmenu_extender.plugin:TopMenuExtenderPlugin',
                          }
    },
    classifiers=[
        'Environment :: Plugins',
        'Environment :: Web Environment',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9'
    ],
)
