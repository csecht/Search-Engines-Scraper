import sys
from os import system

from aggregate_utils import vcheck, get_user_agent, config as cfg

about = {
    'author': 'Craig Echt',
    'copyright': 'Copyright (C) 2022 C.S. Echt',
    'license': 'GNU General Public License',
    'program_name': 'aggregate_search.py',
    'project_url': 'https://github.com/csecht/search-aggregator',
    'version': '0.4.25',
    'credits': 'Tasos M Adamopoulos (tasos-py) and Mario Vilas',
    'dev_environment': 'Python 3.8',
    'status': 'Development Status :: 1 - Alpha',
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
if sys.platform[:3] == 'win':
    system("color")
