from bs4 import BeautifulSoup

from search_engines.engine import SearchEngine
from search_engines.config import PROXY, TIMEOUT


class Metager(SearchEngine):
    """Searches metager.org"""

    def __init__(self, user_agent, proxy=PROXY, timeout=TIMEOUT):
        super().__init__(proxy, timeout)
        self._base_url = 'https://metager.org'
        self.set_headers({'User-Agent': user_agent})

    @staticmethod
    def _selectors(element, **kwargs):
        """Returns the appropriate CSS selector."""
        selectors = {
            'url': 'a.result-link',
            'title': 'h2.result-title a',
            'text': 'div.result-description',
            'links': '#results div.result-header',
            'next': '#next-search-link a',
            }
        return selectors[element]

    def _first_page(self):
        """Returns the initial page and query."""
        query = f'{self._base_url}/meta/meta.ger3?eingabe={self._query}'
        response = self._get_page(query)
        src_pg = BeautifulSoup(response.html, "html.parser")
        url = src_pg.select_one('iframe').get('src')

        return {'url': url, 'data': None}

    def _next_page(self, tags):
        """Returns the next page URL."""
        next_page_tag = tags.select_one(self._selectors('next'))
        url = None
        if next_page_tag:
            next_resp = self._get_page(next_page_tag['href'])
            src_pg = BeautifulSoup(next_resp.html, "html.parser")
            url = src_pg.select_one('iframe').get('src')

        return {'url': url, 'data': None}




