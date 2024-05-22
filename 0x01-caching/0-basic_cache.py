#!/usr/bin/env python3
"""
Basic cache module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache class that inherits from BaseCaching
    """
    def put(self, key, item):
        """ Add an item in cache"""
        if key is None and item is None:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key"""
        if key is not None:
            return self.cache_data.get(key)
