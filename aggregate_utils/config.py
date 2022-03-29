"""
Configuration file used by aggregate_search.py
"""

# Assign a random user agent function from get_user_agents() to each engine.
# Any agent may be temporarily blocked when too frequent requests are made,
#   so try to maximize the choice of most likely to be accepted agents.
# Bot agents, 'bua', are generally banned by SP; tua may be blocked by Moj.
# These tuples of dictionary keys are a mix of static and random user agent
#   functions for random selection by get_user_agents.rando_function().
DDG_UAs = ('bua', 'fua', 'tua', 'eua')
SP_UAs = ('fua', 'wua')
MOJ_UAs = ('bua', 'fua', 'eua', 'rua', 'rua')
MG_UAs = ('bua', 'fua', 'pua', 'tua', 'eua', 'rua')

# Terminal output ANSI foreground colors.
BLUE = '\x1b[1;38;5;33m'
ORANGE = '\x1b[1;38;5;166m'
YELLOW = '\x1b[1;38;5;208m'
NC = '\x1b[0m'  # No color, reset to system default.
