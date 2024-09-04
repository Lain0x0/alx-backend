#!/usr/bin/env python3
""" 3-LRU_Caching """
BaseCaching = __import__("base_caching").BaseCaching


class LRUCache(BaseCaching):
    """ A class LRU """
    def __init__(self):
        """ __Constructor__ """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """ Adding an item in the cache """
        if key is None or item is None:
            return
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key in self.keys:
                self.keys.remove(key)
            self.keys.append(key)
            if len(self.keys) > BaseCaching.MAX_ITEMS:
                first = self.keys.pop(0)
                del self.cache_data[first]
                print("DISCARD: {}".format(first))

    def get(self, key):
        """ Returning the value in self.cache_data """
        if key is None or key not in self.cache_data:
            return None
        if key in self.keys:
            self.keys.remove(key)
            self.keys.append(key)
        return self.cache_data[key]
