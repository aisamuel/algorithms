from sqlite3 import Timestamp
from typing import OrderedDict


from collections import OrderedDict
from time import time

class LastUpdatedOrderedDict(OrderedDict):
    'Store items in the order the keys were last added'

    def __setitem__(self, __k, v) -> None:
        super().__setitem__(__k, v)
        self.move_to_end(__k)


class TimeBoundedLRU:

    def __init__(self, func, maxsize=128, maxage=30):
        self.cache = OrderedDict()
        self.func = func
        self.maxsize = maxsize
        self.maxage = maxage

    def __call__(self, *args):
        if args in self.cache:
            self.cache.move_to_end(args)
            timestamp, result = self.cache[args]
            if time() - timestamp <= self.maxage:
                return result
        result = self.func(*args)
        self.cache[args] = time(), result,
        if len(self.cache) > self.maxsize:
            self.cache.popitem(0)
        return result

class MultiHitLRUCache:

    def __init__(self, func, maxsize=128, maxrequests=4096, cache_after=1):
        self.requests = OrderedDict()
        self.cache = OrderedDict()
        self.func = func
        self.maxrequests = maxrequests
        self.maxsize = maxsize
        self.cache_after = cache_after

    def __call__(self, *args):
        if args in self.cache:
            self.cache.move_to_end(args)
            return self.cache[args]
        result = self.func(*args)
        self.requests[args] = self.requests.get(args, 0) + 1
        if self.requests[args] <= self.cache_after:
            self.requests.move_to_end(*args)
            if len(self.requests) > self.maxrequests:
                self.requests.popitem(0)
        else:
            self.requests.pop(args, None)
            self.cache[args] = result
            if len(self.cache) > self.maxsize:
                self.cache.popitem(0)
        return result