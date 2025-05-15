#!/usr/bin/env python3
""" Defines BasicCache class"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """Basic caching system"""
    def __init__(self):
        """Initialization"""
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            self.cache_data.update({key: item})

    def get(self, key):
        """ Get an item by key
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
