#!/usr/bin/env python3
"""
Data used for --about argument in main script.
"""
from . import __author__, __copyright__, __version__, config as cfg


def data(element) -> dict:
    about_dict = {
        'author': __author__,
        'copyright': __copyright__,
        'license': 'GNU General Public License',
        'program_name': 'aggregate_search.py',
        'project_url': f'{cfg.PROJECT}',
        'version': __version__,
        'dev_environment': 'Python 3.8',
        'status': 'Development Status :: 2 - Beta',
    }
    return about_dict[element]
