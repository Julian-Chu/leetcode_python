'''
Definition of Trip:
class Trip:
    self.id; # trip's id, primary key
    self.driver_id, self.rider_id; # foreign key
    self.lat, self.lng; # pick up location
    def __init__(self, rider_id, lat, lng):

Definition of Helper
class Helper:
    @classmethod
    def get_distance(cls, lat1, lng1, lat2, lng2):
        # return calculate the distance between (lat1, lng1) and (lat2, lng2)
'''
from Trip import Trip, Helper


class Driver:
    def __init__(self, lat, lng, trip_id, available):
        self.lat = lat
        self.lng = lng
        self.trip_id = trip_id
        self.available = available


class MiniUber:

    def __init__(self):
        self.drivers = {}
        self.trips = {}
        self.trip_serial_id = 0

    # @param {int} driver_id an integer
    # @param {double} lat, lng driver's location
    # return {trip} matched trip information if there have matched rider or null
    def report(self, driver_id, lat, lng):
        if driver_id not in self.drivers:
            self.drivers[driver_id] = Driver(lat, lng, 0, True)
            return None
        driver = self.drivers[driver_id]
        driver.lng = lng
        driver.lat = lat
        if driver.trip_id:
            driver.available = False
            return self.trips[driver.trip_id]
        return None

    # @param rider_id an integer
    # @param lat, lng rider's location
    # return a trip
    def request(self, rider_id, lat, lng):
        trip = Trip(rider_id, lat, lng)
        min_dist = float('inf')
        closest_driver_id = -1
        for driver_id, driver in self.drivers.items():
            dist = Helper.get_distance(lat, lng, driver.lat, driver.lng)

            if dist < min_dist:
                min_dist = dist
                closest_driver_id = driver_id

        print(dist, closest_driver_id)
        trip.driver_id = closest_driver_id
        self.trip_serial_id += 1
        self.trips[self.trip_serial_id] = trip
        self.drivers[closest_driver_id].trip_id = self.trip_serial_id

        return trip


'''
Definition of Trip:
class Trip:
    self.id; # trip's id, primary key
    self.driver_id, self.rider_id; # foreign key
    self.lat, self.lng; # pick up location
    def __init__(self, rider_id, lat, lng):

Definition of Helper
class Helper:
    @classmethod
    def get_distance(cls, lat1, lng1, lat2, lng2):
        # return calculate the distance between (lat1, lng1) and (lat2, lng2)
'''
from Trip import Trip, Helper


class Location:

    def __init__(self, lat, lng):
        self.lat = lat
        self.lng = lng


class MiniUber:

    def __init__(self):
        self.driver2Location = {}  # available drivers
        self.driver2Trip = {}

    # @param {int} driver_id an integer
    # @param {double} lat, lng driver's location
    # return {trip} matched trip information if there have matched rider or null
    def report(self, driver_id, lat, lng):
        if driver_id in self.driver2Trip:
            return self.driver2Trip[driver_id]

        if driver_id in self.driver2Location:
            self.driver2Location[driver_id].lat = lat
            self.driver2Location[driver_id].lng = lng
        else:
            self.driver2Location[driver_id] = Location(lat, lng)

        return None

    # @param rider_id an integer
    # @param lat, lng rider's location
    # return a trip
    def request(self, rider_id, lat, lng):
        trip = Trip(rider_id, lat, lng)
        distance, driver_id = -1, -1

        for key, value in self.driver2Location.items():
            dis = Helper.get_distance(value.lat, value.lng, lat, lng)
            if distance < 0 or distance > dis:
                driver_id = key
                distance = dis

        if driver_id != -1:
            del self.driver2Location[driver_id]

        trip.driver_id = driver_id
        self.driver2Trip[driver_id] = trip

        return trip