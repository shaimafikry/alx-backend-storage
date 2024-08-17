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
    def wrapper(url):
        req = method(url)
        key = f"count:{url}"
        cashe_key = f"cache:{url}"
        con.setex(cashe_key, 10, req)
        con.incr(key)
        return req
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
