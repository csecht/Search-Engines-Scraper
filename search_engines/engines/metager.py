from bs4 import BeautifulSoup

from search_engines.engine import SearchEngine
from search_engines.config import PROXY, TIMEOUT


class Metager(SearchEngine):
    """Searches metager3.de/en"""

    def __init__(self, user_agent, proxy=PROXY, timeout=TIMEOUT):
        super().__init__(proxy, timeout)
        # self._base_url = 'https://metager.org'
        self._base_url = 'https://metager3.de/en'
        self.set_headers({'User-Agent': user_agent})

    @staticmethod
    def _selectors(element, **kwargs):
        """Returns the appropriate CSS selector."""
        selectors = {
            'url': 'a.result-link',
            'title': 'h2.result-title a',
            'text': 'div.result-description',
            # 'text': 'a.result-hoster',  # i.e. => by Bing
            'parent': '#results div.result',
            'next': '#next-search-link a',
            }
        return selectors[element]

    def redirect(self, query):
        """Redirects initial request to actual result page."""
        response = self._get_page(query)
        src_page = BeautifulSoup(response.html, "html.parser")
        url = src_page.select_one('#mg-framed').get('src')

        return url

    def _first_page(self):
        """Returns the initial page and query."""
        query = f'{self._base_url}/meta/meta.ger3?eingabe={self.se_query}'
        url = self.redirect(query)

        return {'url': url, 'data': None}

    def _next_page(self, tags):
        """Returns the next page URL."""
        next_page = tags.select_one(self._selectors('next'))
        url = None
        if next_page:
            url = self.redirect(next_page['href'])

        return {'url': url, 'data': None}

