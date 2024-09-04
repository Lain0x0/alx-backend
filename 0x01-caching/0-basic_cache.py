#!/usr/bin/env python3
""" 0-basic_cahe """
BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """ BaseCache class """
    def put(self, key, item):
        """ Add item in cahe """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Return the value in self.cache_data """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
