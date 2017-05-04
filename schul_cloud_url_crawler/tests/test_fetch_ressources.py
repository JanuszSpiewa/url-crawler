from schul_cloud_url_crawler import fetch



def test_fetch_ressource(ressource, ressource_url):
    """Fetch a ressource."""
    result = fetch(ressource_url)
    assert result.get_ressources() == [ressource]


def test_fetch_ressources(ressources, ressource_urls):
    """Test that fetching works for a list of ressources."""
    result = fetch(ressource_urls)
    assert result.get_ressources() == ressources


def test_fetch_list_of_urls(ressources, ressource_urls_url):
    """Fetch a document which contains a list of urls."""
    result = fetch(ressource_urls_url)
    assert result.get_ressources() == ressources





