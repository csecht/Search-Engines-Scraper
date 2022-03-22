
from .duckduckgo import Duckduckgo
from .mojeek import Mojeek
from .startpage import Startpage
# from .metager_inProgress import Metager
from .metager2 import Metager2


search_engines_dict = { 
    'duckduckgo': Duckduckgo,
    'startpage': Startpage,
    # 'metager': Metager,
    'metager2': Metager2,
    'mojeek': Mojeek,
}
