#!/usr/bin/env python3
""" module for redis task"""
import redis
from typing import Any, Callable, Optional, Union, T, List
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
        self._redis.incr(method.__qualname__)
        return method(self, *arg, **kwargs)
    return wrapper

def call_history(method: Callable) -> Callable:
    """ to store the history of inputs and outputs for
    a particular function."""
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        # keys names = methodname: input
        inputs: List = f"{method.__qualname__}:inputs"
        outputs: List = f"{method.__qualname__}:outputs"
        # list for inputs
        self._redis.rpush(inputs, str(args))
        result = method(self, *args, *kwargs)
        # list for outputs
        self._redis.rpush(outputs, str(result))
        return result
    return wrapper


class Cache:
    """ cashe class"""
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
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
