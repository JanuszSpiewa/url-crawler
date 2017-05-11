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


def test_there_are_as_many_resources_as_urls(resources, resource_urls):
    """This is a test test: there should be as many resources as urls.

    The urls point to the resources in this order.
    """
    assert len(resources) == len(resource_urls)


def test_crawled_resources(resources, resource_urls):
    """Test that the resources match."""
    result = fetch(resource_urls)
    assert len(resource_urls) == len(result.crawled_resources)
    for i, crawled_resource in enumerate(result.crawled_resources):
        assert crawled_resource.crawled_resource == resources[i]
        assert crawled_resource.origin_urls == [resource_urls[i]]


def test_index_in_urls(resource_urls_url, resource_urls):
    """Test that the resource urls url is inside the origin."""
    result = fetch(resource_urls_url)
    assert len(resource_urls) == len(result.crawled_resources)
    for i, crawled_resource in enumerate(result.crawled_resources):
         expected_origin_urls = [resource_urls_url + "#" + str(i), resource_urls[i]]
         assert crawled_resource.origin_urls == expected_origin_urls


