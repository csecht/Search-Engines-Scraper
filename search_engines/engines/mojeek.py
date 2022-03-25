from search_engines.engine import SearchEngine
from search_engines.config import PROXY, TIMEOUT


class Mojeek(SearchEngine):
    """Searches mojeek.com"""
    def __init__(self, user_agent, proxy=PROXY, timeout=TIMEOUT):
        super().__init__(proxy, timeout)
        self._base_url = 'https://www.mojeek.com'
        self.set_headers({'User-Agent': user_agent})

    @staticmethod
    def _selectors(element, **kwargs):
        """Returns the appropriate CSS selector."""
        selectors = {
            'url': 'a.ob[href]',
            'title': 'a.ob[href]',
            'text': 'p.s',
            'links': 'ul.results-standard > li',
            'next': {'href': 'div.pagination li a[href]', 'text': 'Next'}
        }
        return selectors[element]

    def _first_page(self):
        """Returns the initial page and query."""
        url = f'{self._base_url}/search?q={self._query}'
        return {'url': url, 'data': None}

    def _next_page(self, tags):
        """Returns the next page URL and post data (if any)"""
        selector = self._selectors('next')
        next_page = [
            i['href'] for i in tags.select(selector['href'])
            if i.text == selector['text']
        ]
        url = (self._base_url + next_page[0]) if next_page else None
        return {'url': url, 'data': None}
