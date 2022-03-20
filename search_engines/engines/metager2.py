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

        url = f'https://metager.org/meta/meta.ger3?eingabe={search}'
        headers = {'user-agent': self.user_agent}
        request = requests.get(url, headers=headers)  # gives <Response [200]>

        links = []
        titles = []
        hosters = []
        if request.status_code == 200:
            soup = BeautifulSoup(request.content, 'html.parser')
            print('Searching metager.org')

            iframe = soup.find('iframe', onload='this.contentWindow.focus();')
            req_url = iframe.get('src')

            request = requests.get(req_url, headers=headers)
            tags = BeautifulSoup(request.content, 'html.parser')

            for h in tags.select('div.result-headline'):
                link_url = h.a['href']
                links.append(link_url)
                result_hoster = h.select_one('a.result-hoster').text.strip()
                hosters.append(result_hoster)

            for t in tags.select('h2.result-title'):
                title = t.select_one('a').text.strip()
                titles.append(title)

        else:
            links.append(f'HTTP Status: {request}, request failed')
            titles.append(f'HTTP Status: {request}, request failed')

        # Need to add the original host to the end of each title.
        titles_plus = list(zip(titles, hosters))
        annotated_titles = [' ->hosted '.join(e) for e in titles_plus]

        return links, annotated_titles
