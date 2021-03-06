# -*- coding: utf8 -*-
# This file is part of PyBossa.
#
# Copyright (C) 2013 SF Isle of Man Limited
#
# PyBossa is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PyBossa is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with PyBossa.  If not, see <http://www.gnu.org/licenses/>.
# Cache global variables for timeouts
"""
This module exports a set of decorators for caching functions.

It exports:
    * cache: for caching functions without parameters
    * memoize: for caching functions using its arguments as part of the key
    * delete_cached: to remove a cached value
    * delete_memoized: to remove a cached value from the memoize decorator

"""
import os
import hashlib
from functools import wraps
from pybossa.core import sentinel

try:
    import cPickle as pickle
except ImportError:  # pragma: no cover
    import pickle

try:
    import settings_local as settings
except ImportError:  # pragma: no cover
    os.environ['PYBOSSA_REDIS_CACHE_DISABLED'] = '1'

ONE_DAY = 24 * 60 * 60
ONE_HOUR = 60 * 60
HALF_HOUR = 30 * 60
FIVE_MINUTES = 5 * 60


def get_key_to_hash(*args, **kwargs):
    """Return key to hash for *args and **kwargs."""
    key_to_hash = ""
    # First args
    for i in args:
        key_to_hash += ":%s" % i
    # Attach any kwargs
    for key in sorted(kwargs.iterkeys()):
        key_to_hash += ":%s" % kwargs[key]
    return key_to_hash


def get_hash_key(prefix, key_to_hash):
    """Return hash for a prefix and a key to hash."""
    key_to_hash = key_to_hash.encode('utf-8')
    key = prefix + ":" + hashlib.md5(key_to_hash).hexdigest()
    return key


def cache(key_prefix, timeout=300):
    """
    Decorator for caching functions.

    Returns the function value from cache, or the function if cache disabled

    """
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            if os.environ.get('PYBOSSA_REDIS_CACHE_DISABLED') is None:  # pragma: no cover
                key = "%s::%s" % (settings.REDIS_KEYPREFIX, key_prefix)
                output = sentinel.slave.get(key)
                if output:
                    return pickle.loads(output)
                else:
                    output = f(*args, **kwargs)
                    sentinel.master.setex(key, timeout, pickle.dumps(output))
                    return output
            else:
                return f(*args, **kwargs)
        return wrapper
    return decorator


def memoize(timeout=300, debug=False):
    """
    Decorator for caching functions using its arguments as part of the key.

    Returns the cached value, or the function if the cache is disabled

    """
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            if os.environ.get('PYBOSSA_REDIS_CACHE_DISABLED') is None:  # pragma: no cover
                key = "%s:%s_args:" % (settings.REDIS_KEYPREFIX, f.__name__)
                key_to_hash = get_key_to_hash(*args, **kwargs)
                key = get_hash_key(key, key_to_hash)
                output = sentinel.slave.get(key)
                if output:
                    return pickle.loads(output)
                else:
                    output = f(*args, **kwargs)
                    sentinel.master.setex(key, timeout, pickle.dumps(output))
                    return output
            else:
                return f(*args, **kwargs)
        return wrapper
    return decorator


def delete_memoized(function, *args, **kwargs):
    """
    Delete a memoized value from the cache.

    Returns True if success

    """
    if os.environ.get('PYBOSSA_REDIS_CACHE_DISABLED') is None:  # pragma: no cover
        key = "%s:%s_args:" % (settings.REDIS_KEYPREFIX, function.__name__)
        key_to_hash = get_key_to_hash(*args, **kwargs)
        key = get_hash_key(key, key_to_hash)
        sentinel.master.delete(key)
        return True


def delete_cached(key):
    """
    Delete a cached value from the cache.

    Returns True if success

    """
    if os.environ.get('PYBOSSA_REDIS_CACHE_DISABLED') is None:  # pragma: no cover
        key = "%s::%s" % (settings.REDIS_KEYPREFIX, key)
        return sentinel.master.delete(key)
