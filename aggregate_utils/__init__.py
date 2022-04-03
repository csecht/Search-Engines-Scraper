#!/usr/bin/env python3
"""
Initialize module information, startup dictionaries and housekeeping.
"""
import os

from . import get_user_agent, vcheck, config as cfg

__author__ = 'Craig S. Echt'
__copyright__ = 'Copyright (C) 2022 C.S. Echt'
__version__ = '0.5.1'

about = {
    'author': __author__,
    'copyright': __copyright__,
    'license': 'GNU General Public License',
    'program_name': 'aggregate_search.py',
    'project_url': 'https://github.com/csecht/search-aggregator',
    'version': __version__,
    'credits': 'Tasos M Adamopoulos (tasos-py) and Mario Vilas',
    'dev_environment': 'Python 3.8',
    'status': 'Development Status :: 2 - Beta',
}

# Random user agents for each engine are assigned here.
agent = {
    'ddg_UA':  get_user_agent.rando_function(cfg.DDG_UAs),
    'sp_UA': get_user_agent.rando_function(cfg.SP_UAs),
    'moj_UA': get_user_agent.rando_function(cfg.MOJ_UAs),
    'mg_UA': get_user_agent.rando_function(cfg.MG_UAs),
}

# Quit if Python interpreter version is earlier than required.
vcheck.minversion('3.6')

# Needed for Windows Command Prompt ANSI text formatting.
if os.name == 'nt':
    os.system("color")
