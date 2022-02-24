#!/usr/bin/env python

from distutils.core import setup

setup(
    name='Cron Explainer',
    version='0.1.0',
    description='Cron explainer parse a cron expresion and translate to a human redable output.',
    author='Diego Peres',
    author_email='speres.diego@gmail.com',
    url='',
    extras_require={
        'dev': [
            'black',
            'pytest',
        ]
    },
    entry_points={
        'console_scripts': [
            'cron-explainer = cron_explainer.main:main',
        ],
    },
)
