#!/usr/bin/env python3

''' Dictionary
'''

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    ''' A class that inherit from BaseCaching
    '''

    def put(self, key, item):
        ''' Add to dictionary
        '''
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        ''' return the value from dictionary by key
        '''

        return self.cache_data.get(key, None)
