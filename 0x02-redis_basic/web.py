#!/usr/bin/env python3
"""
function that uses the requests module
to obtain the HTML content of a particular
URL and returns it.
"""

import redis
import requests

r = redis.Redis()


def cache_page(func):
    """cache page"""

    def wrapper(url):
        """ wrapper """
        key_count = f"count:{url}"
        count_access = r.incr(key_count)

        cache_key = f"cache:{url}"
        cache_res = r.get(cache_key)

        if cache_res:
            return cache_res.decode('utf-8')

        response = requests.get(url)
        content = response.text

        r.setex(cache_key, 10, content)
        return content

    return wrapper


@cache_page
def get_page(url: str) -> str:
    """
    obtain the HTML content of a particular
    URL and returns it.
    """
    return requests.get(url).text
