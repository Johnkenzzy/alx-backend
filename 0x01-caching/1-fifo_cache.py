#!/usr/bin/env python3
"""Defines FIFOCache classs (for FIFO cache replacement policy)"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFO Caching system"""

    def __init__(self):
        """Initialize the cache"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Add an item in the cache using FIFO replacement"""
        if key is None or item is None:
            return

        if key not in self.cache_data:
            self.order.append(key)

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # Discard the first inserted key
            first_key = self.order.pop(0)
            del self.cache_data[first_key]
            print("DISCARD:", first_key)

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
