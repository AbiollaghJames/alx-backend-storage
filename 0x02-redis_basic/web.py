#!/usr/bin/env python3
"""
function that uses the requests module
to obtain the HTML content of a particular
URL and returns it.
"""

import redis
import requests
from functools import wraps
from typing import Callable

r = redis.Redis()


def cache_page(func: Callable) -> Callable:
    """cache page"""

    @wraps(method)
    def wrapper(url):
        """ wrapper """
        r.incr(f"count:{url}")
        cache_res = r.get(f"result: {url}")

        if cache_res:
            return cache_res.decode('utf-8')

        cache_res = method(url)
        r.set(f"count:{url}", 0)
        r.setex(f"result:{url}", 10, cache_res)
        return cache_res

    return wrapper


@cache_page
def get_page(url: str) -> str:
    """
    obtain the HTML content of a particular
    URL and returns it.
    """
    return requests.get(url).text
