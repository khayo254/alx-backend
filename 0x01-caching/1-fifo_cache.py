#!/usr/bin/env python3
""" FIFOCache module
"""
from base_caching import BaseCaching

from collections import OrderedDict


class FIFOCache(BaseCaching):
    """ FIFOCache class that inherits from BaseCaching
    """

    def __init__(self):
        """ Initialize FIFOCache instance
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache with FIFO eviction strategy
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discarded_key = self.queue.pop(0)
            del self.cache_data[discarded_key]
            print("DISCARD:", discarded_key)

    def get(self, key):
        """ Get an item by key
        """
        return self.cache_data(key, None)
