#!/usr/bin/env python3
""" 5-LFU_Caching """
BaseCaching = __import__("base_caching").BaseCaching


class LFUCache(BaseCaching):
    """ A class LFU """
    def __init__(self):
        """ __Constructor__ """
        super().__init__()
        self.keys = {}

    def put(self, key, item):
        """ Adding an item in the cache """
        if key is None or item is None:
            return
        if key is not None and item is not None\
                and self.cache_data.get(key) != item:
            self.cache_data[key] = item
            if len(self.cache_data) > self.MAX_ITEMS:
                lfu_key = min(self.keys, key=self.keys.get)
                self.cache_data.pop(lfu_key)
                self.keys.pop(lfu_key)
                print("DISCARD:", lfu_key)
            self.keys[key] = self.keys.get(key, 0) + 1

    def get(self, key):
        """ Returning the value in self.cache_data """
        if key is None or key not in self.cache_data:
            return None
        if key in self.keys:
            self.keys[key] += 1
        return self.cache_data.get(key)
