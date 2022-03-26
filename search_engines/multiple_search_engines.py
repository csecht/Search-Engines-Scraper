from .results import SearchResults
from .engines import search_engines_dict
from . import output as out
from . import config as cfg


class MultipleSearchEngines:
    """Uses multiple search engines."""
    def __init__(self, engines, agent, proxy=cfg.PROXY, timeout=cfg.TIMEOUT):
        self._engines = [
            se(agent, proxy, timeout)
            for se in search_engines_dict.values()
            if se.__name__.lower() in engines
        ]
        self._filter = None

        self.ignore_duplicate_urls = False
        self.ignore_duplicate_domains = False
        self.results = SearchResults()
        self.banned_engines = []

    def set_search_operator(self, operator):
        """Filters search results based on the operator."""
        self._filter = operator

    def search(self, query, pages=cfg.SEARCH_ENGINE_RESULTS_PAGES):
        """Searches multiples engines and collects the results."""
        for engine in self._engines:
            engine.ignore_duplicate_urls = self.ignore_duplicate_urls
            engine.ignore_duplicate_domains = self.ignore_duplicate_domains
            if self._filter:
                engine.set_search_operator(self._filter)

            engine_results = engine.search(query, pages)
            if engine.ignore_duplicate_urls:
                engine_results.se_results = [
                    item for item in engine_results.se_results
                    if item['link'] not in self.results.links()
                ]
            if self.ignore_duplicate_domains:
                engine_results.se_results = [
                    item for item in engine_results.se_results
                    if item['host'] not in self.results.hosts()
                ]
            self.results.se_results += engine_results.se_results

            if engine.is_banned:
                self.banned_engines.append(engine.__class__.__name__)
        return self.results

    def output(self, output=out.PRINT, path=None):
        """Prints search results and/or creates report files."""
        output = (output or '').lower()
        query = self._engines[0].se_query if self._engines else ''
        if not path:
            path = cfg.OUTPUT_DIR + '_'.join(query.split())
        out.console('')

        if out.PRINT in output:
            out.print_results(self._engines)
        if out.HTML in output:
            out.write_file(out.create_html_data(self._engines), path + '.html')
        if out.CSV in output:
            out.write_file(out.create_csv_data(self._engines), path + '.csv')
        if out.JSON in output:
            out.write_file(out.create_json_data(self._engines), path + '.json')


class AllSearchEngines(MultipleSearchEngines):
    """Uses all search engines."""
    def __init__(self, agent=cfg.USER_AGENT, proxy=cfg.PROXY, timeout=cfg.TIMEOUT):
        super().__init__(
            list(search_engines_dict), agent, proxy, timeout
        )
