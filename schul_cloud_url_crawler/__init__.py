import requests


class Fetcher:

    def __init__(self):
        """Fetch objects from urls."""
        self._ressources = []

    def fetch(self, url):
        """Fetch a url and add the ressources to this fetcher."""
        response = requests.get(url)
        try:
            ressource = response.json()
        except ValueError:
            links = response.text.split()
            for link in links:
                self.fetch(link)
        else:
            self._ressources.append(ressource)

    def get_ressources(self):
        """Return a list of ressources as defined in the api."""
        return self._ressources


def fetch(url_or_list_of_urls):
    """Return a Fetcher that fetches the urls."""
    fetcher = Fetcher()
    if not isinstance(url_or_list_of_urls, list):
        url_or_list_of_urls = [url_or_list_of_urls]
    for url in url_or_list_of_urls:
        fetcher.fetch(url)
    return fetcher