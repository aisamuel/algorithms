from functools import lru_cache
from tkinter import N
import urllib
from urllib import error, request

@lru_cache(maxsize=32)
def get_pep(num):
    resource = 'https://www.python.org/dev/peps/pep-%04d/' % num
    try:
        with request.urlopen(resource) as s:
            return s.read()
    except error.HTTPError:
        return 'Not Found'

for n in 8, 290, 308, 320, 8, 218, 320, 279, 289, 320, 9991:
    pep = get_pep(n)
    print(n, len(pep))

@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

[fib(n) for n in range(16)]
