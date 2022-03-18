from .aol import Aol
from .ask import Ask
from .bing import Bing
from .dogpile import Dogpile
from .duckduckgo import Duckduckgo
from .google import Google
from .mojeek import Mojeek
from .startpage import Startpage
from .torch import Torch
from .yahoo import Yahoo
from .qwant import Qwant
from .metager import Metager
from .metager2 import Metager2
from .brave import Brave


search_engines_dict = { 
    'google': Google, 
    'bing': Bing, 
    'yahoo': Yahoo, 
    'aol': Aol, 
    'duckduckgo': Duckduckgo, 
    'startpage': Startpage,
    'dogpile': Dogpile, 
    'ask': Ask, 
    'mojeek': Mojeek, 
    'qwant': Qwant, 
    'torch': Torch,
    'metager': Metager,
    'metager2': Metager2,
    'brave': Brave
}
