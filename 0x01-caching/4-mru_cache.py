#!/usr/bin/env python3
""" 4-MRU_Caching """
BaseCaching = __import__("base_caching").BaseCaching


class MRUCache(BaseCaching):
    """ A class MRU """
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
                last = self.keys.pop(-2)
                del self.cache_data[last]
                print("DISCARD: {}".format(last))

    def get(self, key):
        """ Returning the value in self.cache_data """
        if key is None or key not in self.cache_data:
            return None
        if key in self.keys:
            self.keys.remove(key)
            self.keys.append(key)
        return self.cache_data[key]
