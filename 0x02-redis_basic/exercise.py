#!/usr/bin/env python3
""" module for redis task"""
import redis
from typing import Any, Callable, Optional
import uuid


class Cache:
    """ cashe class"""
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Any) -> str:
        """ store key """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable]) -> Any:
        """ convert data"""
        value = self._redis.get(key)
        if value is None:
            return None
        if fn:
            return fn(value)
        return value

    def get_str(self, value) -> Optional[str]:
        """ return data as string"""
        pass

    def get_int(self, value) -> Optional[int]:
        """ return data as integer"""
        pass
