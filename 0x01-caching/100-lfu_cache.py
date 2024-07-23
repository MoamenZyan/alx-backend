#!/usr/bin/env python3
"""Least Frequently Used caching module
"""

from base_caching import BaseCaching
from collections import OrderedDict


class LFUCache(BaseCaching):
    """A class that inherit from BaseCaching
    """
    def __init__(self):
        """Initializes cache
        """
        super().__init__()
        self.cache_data = OrderedDict()
        self.keys_freq = []

    def __reorder_items(self, mru_key):
        """reorder items
        """
        position = []
        insert_position = 0
        mru_position = 0
        mru_freq = 0
        for i, key_freq in enumerate(self.keys_freq):
            if key_freq[0] == mru_key:
                mru_freq = key_freq[1] + 1
                mru_position = i
                break
            elif len(position) == 0:
                position.append(i)
            elif key_freq[1] < self.keys_freq[position[-1]][1]:
                position.append(i)
        position.reverse()
        for pos in position:
            if self.keys_freq[pos][1] > mru_freq:
                break
            insert_position = pos
        self.keys_freq.pop(mru_position)
        self.keys_freq.insert(insert_position, [mru_key, mru_freq])

    def put(self, key, item):
        """Add to dictionary
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                lfu_key, _ = self.keys_freq[-1]
                self.cache_data.pop(lfu_key)
                self.keys_freq.pop()
                print("DISCARD:", lfu_key)
            self.cache_data[key] = item
            idx = len(self.keys_freq)
            for i, key_freq in enumerate(self.keys_freq):
                if key_freq[1] == 0:
                    idx = i
                    break
            self.keys_freq.insert(idx, [key, 0])
        else:
            self.cache_data[key] = item
            self.__reorder_items(key)

    def get(self, key):
        """Retrieves an item by key.
        """
        if key is not None and key in self.cache_data:
            self.__reorder_items(key)
        return self.cache_data.get(key, None)
