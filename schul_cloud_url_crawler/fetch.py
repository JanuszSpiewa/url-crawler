import requests


class Fetcher:
    """This holds the state of a fetch operation."""

    def __init__(self):
        """Fetch objects from urls."""
        self._resources = []

    def fetch(self, url):
        """Fetch a url and add the resources to this fetcher."""
        response = requests.get(url)
        try:
            resource = response.json()
        except ValueError:
            links = response.text.split()
            for link in links:
                self.fetch(link)
        else:
            self._resources.append(resource)

    def get_resources(self):
        """Return a list of resources as defined in the api."""
        return self._resources


def fetch(url_or_list_of_urls):
    """Return a Fetcher that fetches the urls."""
    fetcher = Fetcher()
    if not isinstance(url_or_list_of_urls, list):
        url_or_list_of_urls = [url_or_list_of_urls]
    for url in url_or_list_of_urls:
        fetcher.fetch(url)
    return fetcher