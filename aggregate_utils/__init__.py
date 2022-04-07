#!/usr/bin/env python3
"""
Initialize module information, startup dictionaries and housekeeping.
"""
import os

from . import get_user_agent, vcheck, config as cfg

__author__ = 'Craig S. Echt'
__copyright__ = ('Copyright (c) 2022 C.S. Echt,\n'
                 'Copyright (c) 2018 Tasos M Adamopoulos,\n'
                 'Copyright (c) 2009-2020, Mario Vilas')
__version__ = '0.5.6'

about = {
    'author': __author__,
    'copyright': __copyright__,
    'license': 'GNU General Public License',
    'program_name': 'aggregate_search.py',
    'project_url': f'{cfg.PROJECT}',
    'version': __version__,
    'dev_environment': 'Python 3.8',
    'status': 'Development Status :: 2 - Beta',
}

# Random user agents for each engine are assigned here.
# For sensible reporting, item order should match among
#   dict(agents), config.ENGINE_NAMES, and dict(engines)
agents = {
    '(DDG)':  get_user_agent.rando_function(cfg.DDG_UAs),
    '(MG)': get_user_agent.rando_function(cfg.MG_UAs),
    '(SP)': get_user_agent.rando_function(cfg.SP_UAs),
    '(Moj)': get_user_agent.rando_function(cfg.MOJ_UAs),
}

# Quit if Python interpreter version is earlier than required.
vcheck.minversion('3.6')

# Needed for Windows Command Prompt ANSI text formatting.
if os.name == 'nt':
    os.system("color")
