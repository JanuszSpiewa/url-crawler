from pytest import mark
from schul_cloud_url_crawler import CrawledResource



CRAWLER_PROVIDER = {
    "name": "schul_cloud_url_crawler",
    "url": "https://github.com/schul-cloud/schul_cloud_url_crawler",
    "description": "This crawler crawls urls and adds them to the database."
}


def test_crawled_resource_has_resource_inside(resource, crawled_resource):
    """The crawled resource has an attribute for the resource."""
    assert crawled_resource.crawled_resource == resource


def test_crawled_resource_has_urls(crawled_resource, resource_path):
    """The crawled resource has an attribute for the urls it came from."""
    assert crawled_resource.origin_urls == resource_path


get_provider = mark.parametrize("get_provider", [
        lambda cr: cr.resource["providers"][-1],
        lambda cr: cr.provider,
        lambda cr: cr.api_resource_post["data"]["attributes"]["providers"][-1]
    ])


class TestProvider:
    """Test that the provider is computed correctly."""

    @get_provider
    def test_resource_provider_is_set(self, crawled_resource, get_provider):
        """We can retrieve the providers."""
        provider = get_provider(crawled_resource)
        for key, value in CRAWLER_PROVIDER.items():
            assert provider[key] == value

    @get_provider
    def test_source_path_is_in_provider(
            self, crawled_resource, resource_path, get_provider):
        """Make sure the resource path is included in the providers."""
        provider = get_provider(crawled_resource)
        assert provider["url_trace"] == resource_path

    @mark.parametrize("existing_providers", [
            [], None, [{}, {}], ["prov1", "prov2"]
        ])
    def test_provider_is_appended(
            self, resource, resource_path, existing_providers):
        """Test that the provider is appended to the existing ones."""
        if existing_providers is None:
            existing_providers = []
        else:
            resource["providers"] = existing_providers[:]
        crawled_resource = CrawledResource(resource, resource_path)
        providers = crawled_resource.resource["providers"]
        assert len(providers) == len(existing_providers) + 1
        assert providers[:-1] == existing_providers
        assert crawled_resource.crawled_resource.get("providers", []) == existing_providers, "Original resource should not be changed."


class TestApiAdapter:
    """Test the interface which is provided for the api."""

    def test_get_jsonapi_data(self, crawled_resource, resource):
        """Test that the crawled resource can create the right data."""
        resource = crawled_resource.api_resource_post["data"]["attributes"]
        resource.pop("providers")
        assert resource == resource

    def test_id(self, crawled_resource, resource_path):
        """Test that the resources are provided with an id."""

