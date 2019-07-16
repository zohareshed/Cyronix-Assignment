from cached_query_service.dal import BinaryDAL
from cached_query_service.cache_service import CacheService


DEFAULT_MAX_CACHE_SIZE = 4
DEFAULT_MAX_SINGLE_CACHE_IN_BYTES = 65536


class CachedQueryService(object):
    def __init__(self, db_path: str, max_cache_size: int = DEFAULT_MAX_CACHE_SIZE,
                 max_single_entry_size: int = DEFAULT_MAX_SINGLE_CACHE_IN_BYTES):
        self.dal = BinaryDAL(db_path)
        self.cache_service = CacheService(max_cache_size, max_single_entry_size)

    def get_data(self, offset: int, data_length: int) -> bytes:
        cache_key_tuple = (offset, data_length)
        if cache_key_tuple in self.cache_service:
            return self.cache_service.get_cached_object(cache_key_tuple)
        data = self.dal.get_data(offset, data_length)
        self.cache_service.update(cache_key_tuple, data)
        return data
