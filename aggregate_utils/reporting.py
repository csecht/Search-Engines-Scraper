#!/usr/bin/env python3
"""
Combined result reporting for clean terminal/console printing and
writing to file.
"""
import re

from . import files

# Need to remove color escape codes for text in file.
ansi_esc = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')


def report_results(searchterm: str, message: str) -> None:
    """
    Output results or messages to Terminal and file.

    :param searchterm: Current search term; is used for file naming.
    :param message: Message or result string to be printed and written.
    """

    print(message)
    message_cleaned = ansi_esc.sub('', message)
    files.results2file(searchterm, f'{message_cleaned}\n')
