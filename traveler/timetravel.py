import time

class Traveler(object):
    def __init__(self):
        self.store = {}

    def put(self, key, value):
        now = time.time()
        try:
            backing_array = self.store[key]

        except KeyError, e:
            backing_array = []


        backing_array.append((now, value))
        self.store[key] = backing_array

    def get(self, key, time=None):

        try:
            backing_array = self.store[key]
        except KeyError, e:
            return None

        value = backing_array[-1][1]
        if time == None:
            return value
        else:
            return self.find(backing_array, time)

    def find(self, backing_array, time):
        for index, val in enumerate(backing_array):
            if val[0] > time:
                if index == 0:
                    # in the case where you ask for a value from before the beginning of time
                    # return a None value
                    return None
                else:
                    return backing_array[index-1][1]


        return backing_array[-1][1]

class ImprovedTraveler(Traveler):
    def __init__(self):
        super(ImprovedTraveler, self).__init__()

    def find(self, backing_array, time):
        lo = 0
        hi = len(backing_array)

        while lo < hi:
            mid = (lo+hi)//2
            if time < backing_array[mid][0]:
                hi = mid
            else:
                lo = mid+1

        lo = lo - 1
        if lo < 0:
            return None
        return backing_array[lo][1]
