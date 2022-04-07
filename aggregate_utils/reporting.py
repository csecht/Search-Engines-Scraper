#!/usr/bin/env python3
"""
Combined result reporting for clean terminal/console printing and
writing to file.
"""
import re

from . import agents, files, config as cfg


def report_results(search_term: str, message: str) -> None:
    """
    Output results or messages to Terminal and file.

    :param search_term: Current search term; is used for file naming.
    :param message: Message or result string to be printed and written.
    """

    # Need to remove escape codes for text written to file.
    ansi_esc = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')

    print(message)
    message_cleaned = ansi_esc.sub('', message)
    files.results2file(search_term, f'{message_cleaned}\n')


def report_agents(search_term: str) -> None:
    """
    Print to Terminal and result file user agents assigned to each
    engine.

    :param search_term: The input search term; used for file naming.
    """

    user_agents_used = 'User agents assigned for this search:\n'
    for tag in cfg.ENGINE_NAMES:
        user_agents_used = (
            user_agents_used +
            f'{cfg.ENGINE_NAMES[tag].ljust(12)}{cfg.ORANGE}{agents[tag]}{cfg.NC}\n')

    report_results(search_term, user_agents_used)
