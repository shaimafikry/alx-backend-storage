# redis
 - To interact with Redis from Python, you can use the redis-py library.

# Why Use Lambda Here
```
return self.get(key, fn=lambda d: d.decode("utf-8"))

```
or

```
def decode_utf8(data: bytes) -> str:
    return data.decode("utf-8")

# In the Cache class
def get_str(self, key: str) -> str:
    return self.get(key, fn=decode_utf8)

```
Simplicity: The lambda function provides a quick way to define a simple function without needing to formally define a named function elsewhere in the code.
Convenience: It makes the get_str method concise and readable, avoiding the need for additional function definitions for this specific task.

# decorator:

 LOOK AT <a href='https://www.youtube.com/watch?v=r7Dtus7N4pI' >THIS</a>

 CHECK <a href='https://www.geeksforgeeks.org/decorators-in-python'> THIS </a>


# Understanding __qualname__
__qualname__: This attribute provides the qualified name of a method, including the class it belongs to. For example, for a method foo in class Bar, foo.__qualname__ would return 'Bar.foo'.

# @wraps(func)
This is a helper function from the functools module that ensures the decorated function retains the original function’s metadata like its name and docstring.
