#!/usr/bin/env python3
"""get page func"""
import requests
import redis
from typing import Callable
from functools import wraps


con = redis.Redis()


def count_get(method: Callable) -> str:
    """count how many method called"""
    @wraps(method)
    def wrapper(url) -> str:
        key = f"count:{url}"
        result = con.get(f"result:{url}")
        if result:
            return result.decode('utf-8')
        result = method(url)
        con.set(f'count:{url}', 0)
        con.setex(f'result:{url}', 10, result)
        con.incr(key)
        return result
    return wrapper


@count_get
def get_page(url: str) -> str:
    """It uses the requests module to obtain the HTML
    content of a particular URL and returns it."""
    data = requests.get(url)
    return data.text
# if __name__ == "__main__":

# 	url = "http://google.com"
# 	page_content = get_page(url)
# 	print(f"Page content: {len(page_content)}")

# 	# Print the count of accesses
# 	print(f"Access count: {con.get(f'count:{url}').decode('utf-8')}")
