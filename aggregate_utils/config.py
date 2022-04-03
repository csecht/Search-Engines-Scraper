#!/usr/bin/env python3
"""
Configuration file for aggregate_search.py
"""
# Keys here need to match those of the dict(engine) in aggrigate_search.py;
#   item order should also match (b/c used reporting form for loop).
# This is to report the proper/correct engine name.
ENGINE_NAME = {
    '(MG)': 'MetaGer',
    '(DDG)': 'DuckDuckGo',
    '(SP)': 'Startpage',
    '(Moj)': 'Mojeek',
}

# Assign a random user agent function from get_user_agents() to each engine.
# Any agent may be temporarily blocked when too frequent requests are made,
#   so try to maximize the choice of most likely to be accepted agents.
# Bot agents, 'bua', are generally banned by SP; tua may be blocked by Moj.
# These tuples of dictionary keys are a mix of static and random user agent
#   functions for random selection by get_user_agents.rando_function().
DDG_UAs = ('bua', 'fua', 'tua', 'eua')
MG_UAs = ('bua', 'fua', 'pua', 'tua', 'eua', 'rua', 'rua')
MOJ_UAs = ('bua', 'fua', 'eua', 'rua', 'rua')
SP_UAs = ('fua', 'wua')

# Terminal output ANSI foreground colors.
BLUE = '\x1b[1;38;5;33m'
ORANGE = '\x1b[1;38;5;166m'
YELLOW = '\x1b[1;38;5;208m'
NC = '\x1b[0m'  # No color, reset to system default.
