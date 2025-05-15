#!/usr/bin/env python3
"""Defines MRUCache class (for MRU cache replacemenet policy)"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRU Caching system"""

    def __init__(self):
        """Initialize the cache"""
        super().__init__()
        self.usage_order = []

    def put(self, key, item):
        """Add an item in the cache using MRU replacement"""
        if key is None or item is None:
            return

        # If key already exists, remove it from its current position
        if key in self.cache_data:
            self.usage_order.remove(key)

        self.cache_data[key] = item
        self.usage_order.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # Discard the most recently used key (last one in usage_order)
            if self.usage_order[-1] == key:
                mru_key = self.usage_order.pop(-2)
            else:
                self.usage_order.pop(-1)
            del self.cache_data[mru_key]
            print("DISCARD:", mru_key)

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data:
            return None

        # Mark as most recently used
        self.usage_order.remove(key)
        self.usage_order.append(key)

        return self.cache_data[key]
