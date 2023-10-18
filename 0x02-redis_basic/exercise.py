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
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
     a call_history decorator to store the history
     of inputs and outputs for a particular function.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ wrapper """
        key = method.__qualname__
        inpt = key + ":inputs"
        output = key + ":outputs"
        data = str(args)
        self._redis.rpush(inpt, data)
        n = method(self, *args, **kwargs)
        self._redis.rpush(output, str(n))
        return n
    return wrapper


def replay(func: Callable) -> None:
    """
    function to display the history of calls
    of a particular function.
    """
    rs = redis.Redis()
    key = func.__qualname__
    inpt = rs.lrange(f"{key}:inputs", 0, -1)
    output = rs.lrange(f"{key}:outputs", 0, -1)
    calls = len(inpt)
    str_times = "time" if calls == 1 else "times"
    print(f"{key} was called {calls} {str_times}:")

    for inp, outp in zip(inpt, output):
        print(f"{key}(*{inp.decode('utf-8')}) -> {outp.decode('utf-8')}")


class Cache:
    """
    Writing string to Redis
    """
    def __init__(self):
        """ constructor """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        stores input data in Redis
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)

        return key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:

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
