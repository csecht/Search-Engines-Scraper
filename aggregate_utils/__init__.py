
from search_engines.engines.duckduckgo import Duckduckgo
from search_engines.engines.mojeek import Mojeek
from search_engines.engines.startpage import Startpage
from search_engines.engines.metager import Metager

# Engine order here matters for engine-specific reporting
#   of unique results counts.
aggr_engines = {
    '(DDG)': Duckduckgo,
    '(SP)': Startpage,
    '(Moj)': Mojeek,
    '(MG)': Metager,
}

# Used only for reporting proper engine names.
engine_names = {
    '(DDG)': 'DuckDuckGo',
    '(SP)': 'Startpage',
    '(Moj)': 'Mojeek',
    '(MG)': 'MetaGer',
}

# Needed to assign a user agent to each engine with
#   SearchEngine search() in aggregate_search.search_this().
tag_UA = {
    '(DDG)': 'ddg_UA',
    '(SP)': 'sp_UA',
    '(Moj)': 'moj_UA',
    '(MG)': 'mg_UA',
}
