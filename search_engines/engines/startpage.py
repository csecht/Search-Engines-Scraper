from bs4 import BeautifulSoup

from search_engines.engine import SearchEngine
from search_engines.config import PROXY, TIMEOUT
from search_engines import output as out


class Startpage(SearchEngine):
    """Searches startpage.com"""
    def __init__(self, user_agent, proxy=PROXY, timeout=TIMEOUT):
        super().__init__(proxy, timeout)
        self._base_url = 'https://www.startpage.com'
        # FAKE_USER_AGENT OK, random_agent and python_agent ERROR Banned
        self.set_headers({'User-Agent': user_agent})

    @staticmethod
    def _selectors(element, **kwargs):
        """Returns the appropriate CSS selector."""
        selectors = {
            'url': 'a.w-gl__result-url', 
            'title': 'a.w-gl__result-title h3', 
            'text': 'p.w-gl__description', 
            'parent': 'section.w-gl div.w-gl__result',
            'next': {'form': 'form.pagination__form', 'text': 'Next'},
            'search_form': 'form#search input[name]',
            'blocked_form': 'form#blocked_feedback_form'
        }
        return selectors[element]
    
    def _first_page(self):
        """Returns the initial page and query."""
        response = self._get_page(self._base_url)
        tags = BeautifulSoup(response.html, "html.parser")
        selector = self._selectors('search_form')

        data = {
            i['name']: i.get('value', '') 
            for i in tags.select(selector)
        }
        data['query'] = self.se_query
        url = self._base_url + '/sp/search'
        return {'url': url, 'data': data}
    
    def _next_page(self, tags):
        """Returns the next page URL and post data (if any)"""
        selector = self._selectors('next')
        forms = [
            form 
            for form in tags.select(selector['form']) 
            if form.get_text(strip=True) == selector['text']
        ]
        url, data = None, None
        if forms:
            url = self._base_url + forms[0]['action']
            data = {
                i['name']: i.get('value', '')
                for i in forms[0].select('input')
            }
        return {'url': url, 'data': data}
    
    def _is_ok(self, response):
        """Checks if the HTTP response is 200 OK."""
        soup = BeautifulSoup(response.html, 'html.parser')
        selector = self._selectors('blocked_form')
        is_blocked = soup.select_one(selector)
        
        self.is_banned = response.http in [403, 429, 503] or is_blocked
        
        if response.http == 200 and not is_blocked:
            return True
        msg = 'Banned' if is_blocked else ('HTTP ' + str(response.http)) if response.http else response.html
        out.console(msg, level=out.Level.error)
        return False
