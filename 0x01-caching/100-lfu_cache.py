#!/usr/bin/env python3
"""Defines LFUCache classs (for LFU cache replacement policy)"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """LFU Caching system with LRU tie-breaker"""

    def __init__(self):
        """Initialize the cache"""
        super().__init__()
        self.freq = {}
        self.usage_order = []

    def put(self, key, item):
        """Add an item in the cache using LFU replacement"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.freq[key] += 1
            self.usage_order.remove(key)
            self.usage_order.append(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Find the minimum frequency
                min_freq = min(self.freq.values())

                # Collect all keys with this minimum frequency
                lfu_candidates = [
                        k for k in self.freq if self.freq[k] == min_freq]

                # Use LRU policy among the least frequently used
                for k in self.usage_order:
                    if k in lfu_candidates:
                        discard_key = k
                        break

                # Remove from cache, frequency, and usage list
                del self.cache_data[discard_key]
                del self.freq[discard_key]
                self.usage_order.remove(discard_key)
                print("DISCARD:", discard_key)

            # Add new key
            self.cache_data[key] = item
            self.freq[key] = 1
            self.usage_order.append(key)

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data:
            return None

        self.freq[key] += 1
        self.usage_order.remove(key)
        self.usage_order.append(key)
        return self.cache_data[key]
