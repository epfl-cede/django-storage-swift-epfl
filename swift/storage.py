from django.conf import settings

from swift.storage import SwiftStorage, setting

try:
    from django.utils.deconstruct import deconstructible
except ImportError:
    def deconstructible(arg):
        return arg

@deconstructible
class SwiftStorageEpfl(SwiftStorage):
    cache_headers = setting('SWIFT_CACHE_HEADERS', True)

    def __init__(self, **settings):
        self.last_headers_value = None

    def get_headers(self, name):
        if self.cache_headers:
            """
            Optimization : only fetch headers once when several calls are made
            requiring information for the same name.
            When the caller is collectstatic, this makes a huge difference.
            According to my test, we get a *2 speed up. Which makes sense : two
            api calls were made..
            """
            if name != self.last_headers_name:
                # miss -> update
                self.last_headers_value = self.swift_conn.head_object(self.container_name, name)
                self.last_headers_name = name
        else:
            self.last_headers_value = self.swift_conn.head_object(self.container_name, name)
            self.last_headers_name = name

        return self.last_headers_value
