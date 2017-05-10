from .fetch import fetch

class ResourceClient:
    """The client to communicate with the ressource server."""

    def __init__(self, url):
        """Communicate with the server behind the url."""
        self._url = url

    @property
    def url(self):
        """The url of the server."""
        return self._url