class GeoHash:
    """
    @param: geohash: geohash a base32 string
    @return: latitude and longitude a location coordinate pair
    """

    def decode(self, geohash):
        _base32 = "0123456789bcdefghjkmnpqrstuvwxyz"

        geohash_bin = ""

        for ch in geohash:
            geohash_bin += self.i2b(_base32.find(ch))

        longitude_bin = ""
        latitude_bin = ""

        for i in range(len(geohash_bin)):
            if i & 1 == 0:
                longitude_bin += geohash_bin[i]
            else:
                latitude_bin += geohash_bin[i]
        lat = self.decodeBin(-90, 90, latitude_bin)
        lng = self.decodeBin(-180, 180, longitude_bin)
        return (lat, lng)

    def i2b(self, val):
        b = ""
        for _ in range(5):
            if val & 1 == 0:
                b = '0' + b
            else:
                b = '1' + b
            val //= 2
        return b

    def decodeBin(self, left, right, bin_str):
        val = 0
        for b in bin_str:
            mid = (left + right) / 2.0
            if b == '1':
                val = (mid + right) / 2.0
                left = mid
            else:
                val = (left + mid) / 2.0
                right = mid
        return val


class GeoHash:
    """
    @param: geohash: geohash a base32 string
    @return: latitude and longitude a location coordinate pair
    """

    def decode(self, geohash):
        _base32 = "0123456789bcdefghjkmnpqrstuvwxyz"
        b = ""
        for c in geohash:
            b += self.i2b(_base32.find(c))

        odd = ''.join(b[i] for i in range(0, len(b), 2))
        even = ''.join(b[i] for i in range(1, len(b), 2))

        location = []
        location.append(self.get_location(-90.0, 90.0, even))
        location.append(self.get_location(-180.0, 180.0, odd))
        return location

    def i2b(self, val):
        b = ""
        for i in range(5):
            if val % 2:
                b = '1' + b
            else:
                b = '0' + b
            val //= 2
        return b

    def get_location(self, start, end, string):
        for c in string:
            mid = (start + end) / 2.0
            if c == '1':
                start = mid
            else:
                end = mid
        return (start + end) / 2.0