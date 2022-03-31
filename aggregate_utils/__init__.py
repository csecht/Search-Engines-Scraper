import sys

from aggregate_utils import vcheck
from os import system


# Quit if Python interpreter version is earlier than required.
vcheck.minversion('3.6')

# Needed for Windows Command Prompt ANSI text formatting.
if sys.platform[:3] == 'win':
    system("color")
