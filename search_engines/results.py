class SearchResults:
    """Stores the search results"""
    def __init__(self, items=None):
        self.se_results = items or []

    def links(self):
        """Returns the links found in search results"""
        return [row.get('link') for row in self.se_results]

    def titles(self):
        """Returns the titles found in search results"""
        return [row.get('title') for row in self.se_results]

    def text(self):
        """Returns the text found in search results"""
        return [row.get('text') for row in self.se_results]

    def hosts(self):
        """Returns the domains found in search results"""
        return [row.get('host') for row in self.se_results]

    def results(self):
        """Returns all data found in search results"""
        return self.se_results

    def __getitem__(self, index):
        return self.se_results[index]

    def __len__(self):
        return len(self.se_results)

    def __str__(self):
        return f'<SearchResults ({len(self.se_results)} items)>'

    def append(self, item):
        """Appends an item to the results list."""
        self.se_results.append(item)

    def extend(self, items):
        """Appends items to the results list."""
        self.se_results.extend(items)
