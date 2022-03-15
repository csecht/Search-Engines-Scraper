"""
Searches metager.org, does not use engine.SearchEngine.
"""
import requests
from bs4 import BeautifulSoup


class Metager2:
    """
    Searches metager.org, does not use engine.SearchEngine.
    """

    def __init__(self, user_agent):
        self.user_agent = user_agent

    def metager(self, search):

        url = ('https://metager.org/meta/meta.ger3?eingabe=' + search)
        headers = {'user-agent': self.user_agent}
        request = requests.get(url, headers=headers)  # gives <Response [200]>

        links = []
        titles = []
        hosters = []
        if request.status_code == 200:
            soup = BeautifulSoup(request.content, 'html.parser')
            for s in soup.find_all('iframe', {'onload': 'this.contentWindow.focus();'}):
                res_url = s['src']
                request = requests.get(res_url, headers=headers)
                soup = BeautifulSoup(request.content, 'html.parser')

            for i in soup.find_all('h2', {'class': 'result-title'}):
                link_title = i.find('a')
                titles.append(link_title.text.strip())

            for i in soup.find_all('div', {'class': 'result-headline'}):
                result_hoster = i.find('a', attrs={'class': 'result-hoster'})
                hosters.append(result_hoster.text.strip())

            # Prepend https to the base link.
            for i in soup.find_all('a', attrs={'class': 'result-link'}):
                links.append(f'https://{i.text.strip()}')

        else:
            links.append(f'HTTP Status: not 200, request failed')
            titles.append(f'HTTP Status: not 200, request failed')

        # Need to add the original host to the end of each title.
        titles_plus = list(zip(titles, hosters))
        annotated_titles = [' ->hosted '.join(e) for e in titles_plus]

        return links, annotated_titles
