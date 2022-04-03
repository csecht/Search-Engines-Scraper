#!/usr/bin/env python3
"""
Simple check of current Python version.
Functions:
minversion() - Exit program if not minimum required version.
maxversion() - Warn if current is newer than tested versions.
"""

import sys


def minversion(req_version: str) -> None:
    """
    Check current Python version against minimum version required.
    Exit program if current version is less than required.

    :param req_version: The required minimum major and minor version;
        example, '3.6'.
    """
    ver = tuple(map(int, req_version.split('.')))
    if sys.version_info < ver:
        print(f'Sorry, but this program requires Python {req_version} or later.\n'
              'Current Python version:'
              f' {sys.version_info.major}.{sys.version_info.minor}\n'
              'Python downloads are available from https://docs.python.org/')
        sys.exit(0)


def maxversion(req_version: str) -> None:
    """
    Check current Python version against maximum version required.
    Issue warning if current version is more than *req_version*.

    :param req_version: The required maximum major and minor version;
        example, '3.9'.
    """
    ver = tuple(map(int, req_version.split('.')))
    if sys.version_info > ver:
        print(f'NOTICE: this program has not yet been tested with'
              f' Python versions newer than {req_version}.\n'
              'Current Python version:'
              f' {sys.version_info.major}.{sys.version_info.minor}\n')


def about() -> None:
    """
    Print basic information about this module.
    """
    print(__doc__)
    print(f'{"Author:".ljust(11)}', __author__)
    print(f'{"Copyright:".ljust(11)}', __copyright__)
    print(f'{"License:".ljust(11)}', __license__)
    print(f'{"Module:".ljust(11)}', __module_name__)
    print(f'{"Module ver.:".ljust(11)}', __module_ver__)
    print(f'{"Dev Env:".ljust(11)}', __dev_environment__)
    print(f'{"URL:".ljust(11)}', __project_url__)
    print(f'{"Maintainer:".ljust(11)}',  __maintainer__)
    print(f'{"Status:".ljust(11)}', __status__)
    sys.exit(0)


if __name__ == '__main__':
    about()
