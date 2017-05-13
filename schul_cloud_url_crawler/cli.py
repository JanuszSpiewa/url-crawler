"""
The command line interface for the crawler.

TODO:
- delete all
- delete not updated
- delete from urls
- delete not from urls

"""
import click
from schul_cloud_url_crawler.resource_client import ResourceClient
from schul_cloud_resources_api_v1 import ApiClient, ResourceApi
from schul_cloud_resources_api_v1.rest import ApiException
import schul_cloud_resources_api_v1.auth as auth
from urllib3.exceptions import MaxRetryError

UnReachable = (MaxRetryError,)

error_messages = {
    3: "The resources server could be reached but basic authentication failed.",
    4: "The resources server could be reached but API-key authentication failed.",
    5: "The resources server could be reached but it requires authentication with --basic or --apikey.",
    6: "The resource server could not be reached.",
    7: "You can only provide one authentication mechanism with --basic and --apikey.",
    8: "Basic authentication requires a username and a password divided by \":\". Example: --basic=user:password",
}

def error(return_code):
    """Raise an error and explain it."""
    click.echo("Error {}: {}".format(return_code, error_messages[return_code]))
    exit(return_code)


@click.command()
@click.argument("api", type=str, required=True)
@click.argument("urls", type=str, nargs=-1, required=False)
@click.option("--basic", nargs=1, type=str, metavar="username:password", 
              help="Username an password for authentication at the API.")
@click.option("--apikey", nargs=1, type=str, metavar="api-key",
              help="The api key for authentication at the API.")
def main(api, urls=[], basic=None, apikey=None):
    """Fetch ressources from URLS and post them to the API."""
    urls = list(urls)
    api_client = ApiClient(api)
    resource_api = ResourceApi(api_client)
    resource_client = ResourceClient(resource_api)
    print("updating", api, urls, basic, apikey)
    if basic is not None and apikey is not None:
        error(7)
    if basic is not None:
        username_and_password = basic.split(":", 1)
        if len(username_and_password) == 1:
            error(8)
        username, password = username_and_password
        auth.basic(username, password)
        auth_error = 3
    elif apikey is not None:
        auth.api_key(apikey)
        auth_error = 4
    else:
        auth.none()
        auth_error = 5
    try:
        resource_client.update(urls)
    except ApiException as err:
        if err.status == 401:
            click.echo(err.body)
            error(auth_error)
        raise
    except UnReachable:
        error(6)
