#!/usr/bin/env python3

"""
Class Cache that writes string to Redis
"""

import redis
import uuid
from typing import Union, Callable, Optional


class Cache:
    """
    Writing string to Redis
    """
    def __init__(self):
        """ constructor """
        self._redis = redis.Redis()
        self._redis.flushdb()

        def store(self, data: Union[str, bytes, int, float]) -> str:
            """
            stores input data in Redis
            """
            key = str(uuid.uuid4())
            self._redis.set(key, data)

            return key
