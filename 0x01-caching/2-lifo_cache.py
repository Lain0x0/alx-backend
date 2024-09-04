#!/usr/bin/env python3
""" 2-LIFO_Caching """
BaseCaching = __import__("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    """ A class LIFO """
    def __init__(self):
        """ __Constructor__ """
        super().__init__()
        self.last = None

    def put(self, key, item):
        """ Adding item to cache """
        if key is None or item is None:
            return
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                last = self.last
                del self.cache_data[last]
                print("DISCARD: {}".format(last))
            self.last = key

    def get(self, key):
        """ Returning the value """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
