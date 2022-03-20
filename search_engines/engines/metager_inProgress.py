from bs4 import BeautifulSoup

from search_engines.engine import SearchEngine
from search_engines.config import PROXY, TIMEOUT


class Metager(SearchEngine):
    """Searches metager.org"""

    def __init__(self, user_agent, proxy=PROXY, timeout=TIMEOUT):
        super(Metager, self).__init__(proxy, timeout)
        self._base_url = 'https://metager.org'
        self._search_url = 'https://metager.org/meta/meta.ger3?eingabe={}'
        self.set_headers({'User-Agent': user_agent})

    def _selectors(self, element):
        """Returns the appropriate CSS selector."""
        selectors = {
            'url': 'div. result-headline a[href]',
            'title': 'h2.result-title a',
            'text': 'div.result-description',  # <div class="result-body "> <div class="result-description">
            'links': 'a.result-link',
            'next': 'div.next-search-link a[href]', #<div id="next-search-link" > <a  href="https://metager.org/meta/meta.ger3?eingabe=wicken&amp;next=e263a5994e41f05a3b5d1c463fdd2b2e"
            }
        return selectors[element]

    def _first_page(self):
        """Returns the initial page and query."""
        res = self._http_client.get(self._search_url.format(self._query))
        # response = self._get_page(f'{self._base_url}/meta/meta.ger3?eingabe={self._query}')
# <!DOCTYPE html>
        #
        # <html lang="en">
        # <head>
        # <meta charset="utf-8"/>
        # <link href="/index.css?id=b100fecc320a6c9b036975d20f8c56d8" rel="stylesheet"/>
        # <script src="/index.js?id=b100fecc320a6c9b036975d20f8c56d8"></script>
        # <title>india - MetaGer</title>
        # <meta content="width=device-width, initial-scale=1, maximum-scale=1" name="viewport">
        # </meta></head>
        # <body>
        # <iframe autofocus="true" id="mg-framed" onload="this.contentWindow.focus();" src="https://metager.org/meta/meta.ger3?eingabe=india&amp;mgv=b100fecc320a6c9b036975d20f8c56d8"></iframe>
        # </body>
        # </html>

        tags = BeautifulSoup(res.html, "html.parser")

        url = f'{self._base_url}/meta/meta.ger3?eingabe={self._query}'
        return {'url': url, 'data': None}

    def _next_page(self, tags):
        """Returns the next page URL and post data (if any)"""

        # https://metager.org/meta/meta.ger3?eingabe=tractors&next=19a8df3093a9e4c2c0fbbf7e7500a1de

        next_page = tags.select_one(self._selectors('next'))
        url = None
        if next_page:
            url = self._base_url + next_page['href']
        return {'url': url, 'data': None}
