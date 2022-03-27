from pathlib import Path

# Maximum number of pages to search
SEARCH_ENGINE_RESULTS_PAGES = 10 # 20

# HTTP request timeout
TIMEOUT = 12

# Default User-Agent string
USER_AGENT = 'search_engines/0.5 Repo: https://github.com/tasos-py/Search-Engines-Scraper'

# Fake User-Agent string for engines that don't like USER_AGENT.
FAKE_USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; rv:84.0) Gecko/20100101 Firefox/84.0'

# Proxy server
PROXY = None

# Path to output files
OUTPUT_DIR = Path('search_engines/search_results/').resolve()
