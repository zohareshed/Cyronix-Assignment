class CacheService(object):
    def __init__(self, max_cache_size: int, max_single_entry_size: int):
        self.cache = {}
        self.max_cache_size = max_cache_size
        self.max_single_entry_size = max_single_entry_size

    def __contains__(self, key) -> bool:
        """
        Returns True or False depending on whether or not the key is in the cache
        """
        return key in self.cache

    def get_cached_object(self, key):
        """
        This method increments the key access and returns it
        """
        self.cache[key]["times_accessed"] += 1
        return self.cache[key]

    def update(self, key, value) -> None:
        """
        Update the cache dictionary and optionally remove the least used item
        """
        if len(value) > self.max_single_entry_size:
            return
        if key not in self.cache and len(self.cache) >= self.max_cache_size:
            self._remove_least_used_entry()

        self.cache[key] = {'times_accessed': 0, 'value': value}

    def _remove_least_used_entry(self) -> None:
        """
        Remove the least used entry
        """
        least_used_entry = None
        for key in self.cache:
            if least_used_entry is None:
                least_used_entry = key
            elif self.cache[key]['times_accessed'] < self.cache[least_used_entry]['times_accessed']:
                least_used_entry = key
        self.cache.pop(least_used_entry)
