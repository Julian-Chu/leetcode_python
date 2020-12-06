class GeoHash:
    """
    @param: latitude: one of a location coordinate pair
    @param: longitude: one of a location coordinate pair
    @param: precision: an integer between 1 to 12
    @return: a base32 string
    """
    base32str = "0123456789bcdefghjkmnpqrstuvwxyz"

    def encode(self, latitude, longitude, precision):
        count = precision * 5 // 2 + 1  # how many time binary search
        longitudeRange = (-180, 180)
        latitudeRange = (-90, 90)

        longitudeHash = self.calc(longitudeRange, longitude, count, [])
        latitudeHash = self.calc(latitudeRange, latitude, count, [])
        geohashlist = [0] * (count * 2)

        for i in range(count):
            geohashlist[i * 2] = longitudeHash[i]
            geohashlist[i * 2 + 1] = latitudeHash[i]

        result = ""
        val = 0
        for i in range(len(geohashlist)):
            val = val << 1
            val += geohashlist[i]
            if (i + 1) % 5 == 0:
                result += self.base32str[val]
                val = 0

        return result[:precision]

    def calc(self, ValueRange, degree, count, result):
        if count == 0:
            return result
        left, right = ValueRange
        mid = (left + right) / 2

        if degree > mid:
            result.append(1)
            ValueRange = (mid, right)
        else:
            result.append(0)
            ValueRange = (left, mid)

        return self.calc(ValueRange, degree, count - 1, result)

class GeoHash:
    # @param {double} latitude, longitude a location coordinate pair
    # @param {int} precision an integer between 1 to 12
    # @return {string} a base32 string
    def encode(self, latitude, longitude, precision):
        # Write your code here
        _base32 = "0123456789bcdefghjkmnpqrstuvwxyz"
        lat_bin = self.get_bin(latitude, -90, 90)
        lng_bin = self.get_bin(longitude, -180, 180)

        hash_code, b = '', ''
        for i in range(30):
            b += lng_bin[i] + lat_bin[i]

        for i in range(0, 60, 5):
            hash_code += _base32[int(b[i:i + 5], 2)]

        return hash_code[:precision]

    def get_bin(self, value, left, right):
        b = ''
        for i in range(30):
            mid = (left + right) / 2.0
            if value > mid:
                left = mid
                b += '1'
            else:
                right = mid
                b += '0'
        return b