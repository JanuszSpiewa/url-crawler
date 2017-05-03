url-crawler
===========


This crawler fetches ressources from urls and posts them to a server.

Purpose
-------

The purpose of this crawler is:

- We can provide tests data to the API.
- It can crawl ressources which are not active and cannot post.
- It has the full crawler logic but does not transform into other formats.

  - Maybe we can create recommendations or a library for crawlers from this case.

The crawler should work as follows:

- Provide urls

  - as command line arguments
  - as a link to a file with one url per line
  
- Provide ressources_

  - as one ressource in a file
  - as a list of ressources

The crawler must be invoked to crawl.

This example gets a ressource from the url and post it to the api.

.. code:: shell

    python3 -m ressource_url_crawler     \
            --api=http://localhost:8080  \
            --url=https://raw.githubusercontent.com/schul-cloud/ressources-api-v1/master/schemas/ressource/examples/valid/example-website.json

Further Requirements:

- **The crawler does not post ressources twice.**
  This can be implemented by
  
  - caching the ressources localy, to see if they changed
  
    - compare ressource
    - compare timestamp
    
  - removing the ressources from the database if they are updated after posting new ressources


.. _ressources: https://github.com/schul-cloud/ressources-api-v1#ressources-api
