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
            return self.cache_data.get(key, None)

# Testing the BasicCache class
if __name__ == "__main__":
    my_cache = BasicCache()

    my_cache.put("key1", "value1")
    my_cache.put("key2", "value2")

    my_cache.print_cache()

    print(my_cache.get("key1"))
    print(my_cache.get("key3"))
