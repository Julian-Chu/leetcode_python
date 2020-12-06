'''
Definition of Location:
class Location:
    # @param {double} latitude, longitude
    # @param {Location}
    @classmethod
    def create(cls, latitude, longitude):
        # This will create a new location object

Definition of Restaurant:
class Restaurant:
    # @param {str} name
    # @param {Location} location
    # @return {Restaurant}
    @classmethod
    def create(cls, name, location):
        # This will create a new restaurant object,
        # and auto fill id

Definition of Helper
class Helper:
    # @param {Location} location1, location2
    @classmethod
    def get_distance(cls, location1, location2):
        # return calculate the distance between two location

Definition of GeoHash
class GeoHash:
    # @param {Location} location
    # @return a string
    @classmethom
    def encode(cls, location):
        # return convert location to a geohash string

    # @param {str} hashcode
    # @return {Location}
    @classmethod
    def decode(cls, hashcode):
        # return convert a geohash string to location
'''
from YelpHelper import Location, Restaurant, GeoHash, Helper


class MiniYelp:
    def __init__(self):
        self.id2restaurant = {}
        self.restaurant_serial_id = 0
        self.geohash_table = {}

    # @param {str} name
    # @param {Location} location
    # @return {int} restaurant's id
    def add_restaurant(self, name, location):
        restaurant = Restaurant(name, location)

        self.restaurant_serial_id += 1
        restaurant_id = self.restaurant_serial_id
        self.id2restaurant[restaurant_id] = restaurant

        geohash = GeoHash.encode(location)
        for i in range(0, 6):
            key = geohash[:i]
            if key not in self.geohash_table:
                self.geohash_table[key] = set()
            self.geohash_table[key].add(restaurant_id)
        return restaurant_id

    # @param {int} restaurant_id
    # @return nothing
    def remove_restaurant(self, restaurant_id):
        if restaurant_id in self.id2restaurant:
            restanrant = self.id2restaurant[restaurant_id]
            del self.id2restaurant[restaurant_id]
            geohash = GeoHash.encode(restanrant.location)
            for i in range(0, 6):
                key = geohash[:i]
                if key not in self.geohash_table:
                    continue
                self.geohash_table[key].remove(restaurant_id)

    # @param {Location} location
    # @param {double} k, distance smaller than k miles
    # @return {str[]} a list of restaurant's name and sort by
    # distance from near to far.
    def neighbors(self, location, k):
        geohash_len = self.get_geohash_length(k)
        if geohash_len > 5:
            geohash_len = 5
        cur_geohash = GeoHash.encode(location)
        key = cur_geohash[:geohash_len]
        if key not in self.geohash_table:
            return []

        restaurants_id = self.geohash_table[key]

        restaurants = [(
            self.id2restaurant[restaurant_id].name,
            Helper.get_distance(location, self.id2restaurant[restaurant_id].location))
            for restaurant_id in restaurants_id]
        print(restaurants)
        restaurants.sort(key=lambda restaurant: restaurant[1])
        return [name for (name, dist) in restaurants if dist < k]

    def get_geohash_length(self, k):
        kmError = [2500, 630, 78, 20, 2.4, 0.61, 0.076, 0.01911, 0.00478]

        for i, dist in enumerate(kmError):
            if k > dist:
                return i

        return -1

from YelpHelper import Location, Restaurant, GeoHash, Helper
import bisect

class MiniYelp:

    def __init__(self):
        # initialize your data structure here.
        self.restaurants = {}
        self.ids = {}
        self.geo_value  = []

    # @param {str} name
    # @param {Location} location
    # @return {int} restaurant's id
    def add_restaurant(self, name, location):
        # Write your code here
        restaurant = Restaurant.create(name, location)
        hashcode = "%s.%s" % (GeoHash.encode(location), restaurant.id)
        bisect.insort(self.geo_value, hashcode)
        self.restaurants[hashcode] = restaurant
        self.ids[restaurant.id] = hashcode
        return restaurant.id

    # @param {int} restaurant_id
    # @return nothing
    def remove_restaurant(self, restaurant_id):
        # Write your code here
        hashcode = self.ids[restaurant_id]
        index = bisect.bisect_left(self.geo_value, hashcode)
        self.geo_value.pop(index)
        del self.restaurants[hashcode]
        del self.ids[restaurant_id]

    # @param {Location} location
    # @param {double} k, distance smaller than k miles
    # @return a list of restaurant's name and sort by
    # distance from near to far.
    def neighbors(self, location, k):
        # Write your code here
        length = self.get_length(k)
        hashcode = GeoHash.encode(location)[0:length]
        print(hashcode)
        print(hashcode + '{')  # '{' is closest char greater 'z'
        print(self.geo_value)
        left = bisect.bisect_left(self.geo_value, hashcode)
        right = bisect.bisect_right(self.geo_value, hashcode + '{')

        print(left, right)
        results = []
        # print left, right, hashcode
        for index in range(left, right):
            hashcode = self.geo_value[index]
            restaurant = self.restaurants[hashcode]
            distance = Helper.get_distance(location, restaurant.location)
            if  distance <= k:
                results.append((distance, restaurant))

        results = sorted(results, key=lambda obj: obj[0])
        return [rt[1].name for rt in results]

    def get_length(self, k):
        ERROR = [2500, 630, 78, 20, 2.4, 0.61, 0.076, 0.01911, 0.00478, 0.0005971, 0.0001492, 0.0000186]
        for i, error in enumerate(ERROR):
            if k  > error:
                return i

        return len(ERROR)