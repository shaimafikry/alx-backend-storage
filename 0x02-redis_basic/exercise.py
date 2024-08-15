#!/usr/bin/env python3
""" module for redis task"""
import redis
from typing import Any, Callable, Optional, Union, T
import uuid
import functools


# Above Cache define a count_calls decorator that takes
# a single method Callable argument and returns a Callable.
def count_calls(method: Callable) -> Callable:
    """ count calls"""
    @functools.wraps(method)
    # this func gonna create anew key wth the method name
    # and increse its value every time it's called
    def wrapper(self, *arg, **kwargs):
        """ the wrraper func"""
        # attribute provides the qualified name of a method,
        # including the class it belongs to. For example, for
        # amethod foo in class Bar, foo.__qualname__ would
        # return'Bar.foo'.
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *arg, **kwargs)
    return wrapper


class Cache:
    """ cashe class"""
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ store key """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Optional[Callable[[Any], Any]] = None) -> Optional[Any]:
        """ convert data"""
        value = self._redis.get(key)
        if value is None:
            return None
        if fn:
            return fn(value)
        return value

    def get_str(self, key: str) -> Optional[str]:
        """ return data as string"""
        return self.get(key, fn=lambda k: k.decode('utf-8'))

    def get_int(self, key: str) -> Optional[int]:
        """ return data as integer"""
        return self.get(key, fn=int)
