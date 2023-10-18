#!/usr/bin/env python3

"""
Class Cache that writes string to Redis
"""

import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    function that increments the count for that key every
    time the method is called and returns the value returned
    by the original method
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """wrapper"""
        key = method.__qualname__
        self._redis.incr(key, 0) + 1
        return method(self, *args, **kwargs)
    return wrapper

class Cache:
    """
    Writing string to Redis
    """
    def __init__(self):
        """ constructor """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        stores input data in Redis
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)

        return key

    def get(
        self, key: str, fn: Optional[Callable] = None
        ) -> Union[str, bytes, int, float]:

        """
        convert the data back to the desired format
        """
        val = self._redis.get(key)

        return val if not fn else fn(val)

    def get_str(self, key):
        val = self._redis.get(key)
        return val.decode('utf-8')

    def get_int(self, key):
        return self.get(key, int)
