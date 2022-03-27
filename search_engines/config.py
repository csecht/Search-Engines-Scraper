from pathlib import Path
from sys import version_info

# Python version
PYTHON_VERSION = version_info.major

# Maximum number of pages to search
SEARCH_ENGINE_RESULTS_PAGES = 10 # 20

# HTTP request timeout
TIMEOUT = 12

# Default User-Agent string
USER_AGENT = 'search_engines/0.5 Repo: https://github.com/tasos-py/Search-Engines-Scraper'

# Fake User-Agent string - Google desn't like the default user-agent
FAKE_USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; rv:84.0) Gecko/20100101 Firefox/84.0'

# Proxy server
PROXY = None

# TOR proxy server
TOR = 'socks5h://127.0.0.1:9050'

# Path to output files
OUTPUT_DIR = Path('search_engines/search_results/').resolve()
