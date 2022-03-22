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

        search_url = f'https://metager.org/meta/meta.ger3?eingabe={search}'
        headers = {'user-agent': self.user_agent}
        request = requests.get(search_url, headers=headers)

        links = []
        titles = []
        hosters = []
        if request.status_code == 200:
            soup = BeautifulSoup(request.content, 'html.parser')
            print('Searching metager.org')

            source_pg = soup.select_one('iframe').get('src')

            page_req = requests.get(source_pg, headers=headers)
            tags = BeautifulSoup(page_req.content, 'html.parser')

            for h in tags.select('div.result-headline'):
                links.append(h.a['href'])

                result_hoster = h.select_one('a.result-hoster').text.strip()
                hosters.append(result_hoster)

            for t in tags.select('h2.result-title'):
                title = t.select_one('a').text.strip()
                titles.append(title)

        else:
            links.append(f'HTTP Status: {request}, request failed')
            titles.append(f'HTTP Status: {request}, request failed')

        # Need to add the original host to the end of each title.
        titles_and_hosts = list(zip(titles, hosters))
        annotated_titles = [' ->hosted '.join(item) for item in titles_and_hosts]

        return links, annotated_titles
