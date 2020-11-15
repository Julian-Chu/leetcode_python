class Cache:
    def __init__(self, curtTime, value, ttl):
        self.value = value
        self.expired_at = curtTime + ttl - 1
        if ttl == 0:
            self.expired_at = -1


KeyNotExist = 2147483647


class Memcache:
    def __init__(self):
        self.cacheDic = {}

    """
    @param: curtTime: An integer
    @param: key: An integer
    @return: An integer
    """

    def get(self, curtTime, key):
        # write your code here
        if key not in self.cacheDic:
            return KeyNotExist

        cache = self.cacheDic.get(key)
        if cache.expired_at >= curtTime or cache.expired_at == -1:
            return cache.value

        return KeyNotExist

    """
    @param: curtTime: An integer
    @param: key: An integer
    @param: value: An integer
    @param: ttl: An integer
    @return: nothing
    """

    def set(self, curtTime, key, value, ttl):
        self.cacheDic[key] = Cache(curtTime, value, ttl)

    """
    @param: curtTime: An integer
    @param: key: An integer
    @return: nothing
    """

    def delete(self, curtTime, key):
        self.cacheDic.pop(key, None)

    """
    @param: curtTime: An integer
    @param: key: An integer
    @param: delta: An integer
    @return: An integer
    """

    def incr(self, curtTime, key, delta):
        if self.get(curtTime, key) == KeyNotExist:
            return KeyNotExist
        self.cacheDic[key].value += delta
        return self.cacheDic[key].value

    """
    @param: curtTime: An integer
    @param: key: An integer
    @param: delta: An integer
    @return: An integer
    """

    def decr(self, curtTime, key, delta):
        if self.get(curtTime, key) == KeyNotExist:
            return KeyNotExist
        self.cacheDic[key].value -= delta
        return self.cacheDic[key].value
