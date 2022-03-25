import json
import re

from bs4 import BeautifulSoup

from .. import utils
from ..config import PROXY, TIMEOUT
from ..engine import SearchEngine


class Duckduckgo(SearchEngine):
    """Searches duckduckgo.com"""

    def __init__(self, user_agent, proxy=PROXY, timeout=TIMEOUT):
        super().__init__(proxy, timeout)
        self._base_url = 'https://links.duckduckgo.com{}&biaexp=b&msvrtexp=b&videxp=a&nadse=b&tjsexp=b'
        self._main_url = 'https://duckduckgo.com/?q={}&t=h_'
        self._current_page = None
        self.set_headers({'User-Agent': user_agent})

    @staticmethod
    def _selectors(element, **kwargs):
        """Returns the appropriate CSS selector - regex pattern, in this case."""
        selectors = {
            'first_page': r'DDG\.deep\.initialize\(\'(.*?)\'\)',
            'next_page': r'"n"\:\s*"(/d\.js.*?)"',
            'results': r"DDG\.pageLayout\.load\('d'\,\s*(\[.*?\])\s*\);"
        }
        return selectors[element]

    def _first_page(self):
        """Returns the initial page and query."""
        res = self._http_client.get(self._main_url.format(self._query))
        match = re.search(self._selectors('first_page'), res.html)
        if match:
            return {'url': self._base_url.format(match.group(1)), 'data': None}
        return {'url': None, 'data': None}

    def _next_page(self, tags):
        """Returns the next page URL and post data (if any)"""
        match = re.search(self._selectors('next_page'), tags.get_text())
        if match:
            return {'url': self._base_url.format(match.group(1)), 'data': None}
        return {'url': None, 'data': None}

    def _get_page(self, page, data=None):
        """Gets pagination links."""
        self._http_client.session.headers['Referer'] = 'https://duckduckgo.com/'
        response = self._http_client.get(page)
        self._current_page = response.html
        return response

    def _filter_results(self, soup):
        """Processes and filters the search results."""
        match = re.search(self._selectors('results'), self._current_page)
        if not match:
            return {}
        data = json.loads(re.sub('\n|\r', '', match.group(1)))[:-1]
        results = [
            {'link': i['u'], 'title': i['t'],
             'text': BeautifulSoup(i['a'], 'html.parser').get_text()}
            for i in data
        ]

        if 'url' in self._filters:
            results = [_l for _l in results if self._query_in(_l['link'])]
        if 'title' in self._filters:
            results = [_l for _l in results if self._query_in(_l['title'])]
        if 'text' in self._filters:
            results = [_l for _l in results if self._query_in(_l['text'])]
        if 'host' in self._filters:
            results = [_l for _l in results if self._query_in(utils.domain(_l['link']))]
        return results
