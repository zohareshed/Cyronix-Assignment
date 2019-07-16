# Cyronix-Assignment

This module implements a caching system for the binary db.
The caching mechanism works by storing the most accessed entries at any given moment.

After exploring the procmon log, I've seen there's 4 queries which are called way more often, and that's why the caching mechanism stores 4 entries by default.
That way even if the queries will change it will still be effective.

###Running
Simply run the new cached db service by creating a CachedQueryService object.
Then call the method "get_data".

####NOTE
Because the db is just for reading, the caching mechanism doesn't renew the entries.