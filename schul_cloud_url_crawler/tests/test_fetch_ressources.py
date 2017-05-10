from schul_cloud_url_crawler import fetch



def test_fetch_resource(resource, resource_url):
    """Fetch a resource."""
    result = fetch(resource_url)
    assert result.get_resources() == [resource]


def test_fetch_resources(resources, resource_urls):
    """Test that fetching works for a list of resources."""
    result = fetch(resource_urls)
    assert result.get_resources() == resources


def test_fetch_list_of_urls(resources, resource_urls_url):
    """Fetch a document which contains a list of urls."""
    result = fetch(resource_urls_url)
    assert result.get_resources() == resources


def test_fetch_invalid_example():
    assert False


def test_fetch_invalid_url():
    assert False


