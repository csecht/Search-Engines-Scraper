"""
Author, development, and usage information.
"""
import __main__
from pathlib import Path
from sys import exit as sys_exit

from . import __author__, __copyright__, __version__, config as cfg


def info(main_doc: str) -> None:
    """
    Run in response to -i or --info cmd line arg.

    :param main_doc: The __doc__ docstring from the main script.
    """
    data = {
        'author': __author__,
        'copyright': __copyright__,
        'license': 'GNU General Public License and others',
        'program_name': 'aggregate_search.py',
        'project_url': f'{cfg.PROJECT}',
        'version': __version__,
        'dev_environment': 'Python 3.8',
        'status': 'Development Status :: 2 - Beta',
    }
    print(main_doc)
    print(f'{"Author:".ljust(10)}', data['author'])
    print(f'{"License:".ljust(10)}', data['license'])
    print(f'{"Copyright:".ljust(10)}', data['copyright'])
    print(f'{"Program:".ljust(10)}', data['program_name'])
    print(f'{"URL:".ljust(10)}', data['project_url'])
    print(f'{"Version:".ljust(10)}', data['version'])
    print(f'{"Dev Env:".ljust(10)}', data['dev_environment'])
    print(f'{"Status:".ljust(10)}', data['status'])
    print()
    sys_exit(0)


def usage():
    """
    Print short usage explanation, then print text from use_syntax file.
    """
    print(f'{cfg.ORANGE}USAGE: Run {__main__.__file__} without arguments or with the [--x] option,\n'
          f'       then enter your search term at the prompt.{cfg.NC}\n')
    _use = Path('aggregate_utils/use_syntax.txt').resolve()
    try:
        syntax = Path(_use).read_text(encoding='utf-8')
        print(syntax)
    except FileNotFoundError:
        print(f'Sorry, but could not find file: {_use}')
    sys_exit(0)
