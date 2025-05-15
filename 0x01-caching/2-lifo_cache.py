#!/usr/bin/env python3
"""Defines LIFOCache class (for LIFO cache replacement policy)"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFO Caching system"""

    def __init__(self):
        """Initialize the cache"""
        super().__init__()
        self.last_key = None

    def put(self, key, item):
        """Add an item in the cache using LIFO replacement"""
        if key is None or item is None:
            return

        self.cache_data[key] = item
        self.last_key = key

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # Discard the last item added (LIFO)
            keys = list(self.cache_data.keys())
            discard_key = keys[-2] if self.last_key == keys[-1] else keys[-1]
            del self.cache_data[discard_key]
            print("DISCARD:", discard_key)

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
