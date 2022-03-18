"""
Searches search.brave.com, returns links and titles;
does not use engine.SearchEngine.
"""
import requests
from bs4 import BeautifulSoup


class Brave:
    """
    Searches search.brave.com; does not use engine.SearchEngine.
    """

    def __init__(self, user_agent):
        self.user_agent = user_agent

    def brave(self, search: str) -> tuple:
        """
        Using header data from system's Firefox browser from http://myhttpheader.com

        :param search: The search term.
        :return: Tuple of found [links] and [titles].
        """
        url = f'https://search.brave.com/search?q={search}'
        headers = {
            'user-agent': self.user_agent,
            'request-line': "GET / HTTP/1.1",
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'accept-encoding': 'gzip, deflate',
            'accept-language': 'en-US,en;q=0.5',
            'connection': 'keep-alive',
            'sec-gpc': '1',
            'upgrade-insecure-requests': '1',
             }
        request = requests.get(url, headers=headers)  # gives <Response [200]>

        links = []
        titles = []
        if request.status_code == 200:
            soup = BeautifulSoup(request.content, 'html.parser')
            print('Searching Brave')

            for snip in soup.find_all('div', {'class': 'snippet fdb'}):
                link_url = snip.a['href']
                links.append(link_url)

            for title in soup.find_all('span', {'class': 'snippet-title'}):
                titles.append(title.text.strip())

        else:
            links.append(f'HTTP Status: {request}, request failed')
            titles.append(f'HTTP Status: {request}, request failed')

        return links, titles
