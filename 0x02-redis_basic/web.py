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
"""redis instance"""


def cache_page(func: Callable) -> Callable:
    """cache page"""

    @wraps(func)
    def wrapper(url) -> str:
        """ wrapper """
        r.incr(f"count:{url}")
        cache_res = r.get(f"cache result: {url}")

        if cache_res:
            return cache_res.decode('utf-8')

        cache_res = func(url)
        r.set(f"count:{url}", 0)
        r.setex(f"cache result:{url}", 10, cache_res)
        return cache_res

    return wrapper


@cache_page
def get_page(url: str) -> str:
    """
    obtain the HTML content of a particular
    URL and returns it.
    """
    return requests.get(url).text
