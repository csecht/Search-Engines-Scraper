"""
Configuration file for aggregate_search.py
"""

PROJECT = 'https://github.com/csecht/search-aggregator'

# For sensible reporting, item order should match among
#   dict(agents), config.ENGINE_NAMES, and dict(engines)
ENGINE_NAMES = {
    '(DDG)': 'DuckDuckGo',
    # '(MG)': 'MetaGer',
    '(SP)': 'Startpage',
    '(Moj)': 'Mojeek',
}

# Assign a random user agent function from get_user_agents() to each engine.
# Any agent may be temporarily blocked when too frequent requests are made,
#   so try to maximize the choice of most likely to be accepted agents.
# Bot agents, 'bua', are generally banned by SP & Moj;
#   'gua' sometimes by Moj; 'rua' often by SP.
# These tuples of dictionary keys are a mix of static and random user agent
#   functions randomly selected by the get_user_agents.rando_function().
DDG_UAs = ('bua', 'fua', 'wua', 'gua')
# MG_UAs = ('bua', 'fua', 'wua', 'pua', 'gua', 'rua', 'rua')
MOJ_UAs = ('fua', 'wua', 'rua', 'rua')
SP_UAs = ('fua', 'wua')

# Terminal output ANSI foreground colors.
BLUE = '\x1b[1;38;5;33m'
ORANGE = '\x1b[1;38;5;166m'
YELLOW = '\x1b[1;38;5;208m'
NC = '\x1b[0m'  # No color, reset to system default.
