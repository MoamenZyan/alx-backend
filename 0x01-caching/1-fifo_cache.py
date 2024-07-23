#!/usr/bin/env python3

'''FIFO caching
'''

from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    '''A class that inherit from BaseCaching
    '''

    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        '''add to dictionary
        '''

        if key is None or item is None:
            return

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(last=False)
            print(f"DISCARD: {first_key}")

        self.cache_data[key] = item

    def get(self, key):
        '''return the value from dictionary by key
        '''
        return self.cache_data.get(key, None)
