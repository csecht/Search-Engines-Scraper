import sys
from os import system

from aggregate_utils import vcheck

about = {
    'author': 'Craig Echt',
    'copyright': 'Copyright (C) 2022 C.S. Echt',
    'license': 'GNU General Public License',
    'program_name': 'aggregate_search.py',
    'project_url': 'https://github.com/csecht/search-aggregator',
    'version': '0.4.23',
    'credits': 'Tasos M Adamopoulos (tasos-py) and Mario Vilas',
    'dev_environment': 'Python 3.8',
    'status': 'Development Status :: 1 - Alpha',
}

# Quit if Python interpreter version is earlier than required.
vcheck.minversion('3.6')

# Needed for Windows Command Prompt ANSI text formatting.
if sys.platform[:3] == 'win':
    system("color")
