#!/usr/bin/env python3
"""Defines LRUCache class (for LRU caching replacement policy)"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRU Caching system"""

    def __init__(self):
        """Initialize the cache"""
        super().__init__()
        self.usage_order = []

    def put(self, key, item):
        """Add an item in the cache using LRU replacement"""
        if key is None or item is None:
            return

        # If key already exists, remove it from current position
        if key in self.cache_data:
            self.usage_order.remove(key)

        self.cache_data[key] = item
        self.usage_order.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # Remove the least recently used key
            lru_key = self.usage_order.pop(0)
            del self.cache_data[lru_key]
            print("DISCARD:", lru_key)

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data:
            return None

        # Move the key to the end to mark it as recently used
        self.usage_order.remove(key)
        self.usage_order.append(key)

        return self.cache_data[key]
