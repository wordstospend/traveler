import unittest
import time
from traveler.timetravel import *

class TimeTravelTest(unittest.TestCase):
    def setUp(self):
        self.tt = Traveler()

    def positive_test(self):
        early = time.time()
        time.sleep(.01)
        self.tt.put('one', 1)
        v = self.tt.get('one')
        self.assertEqual(v, 1)
        v2 = self.tt.get('one', early)
        self.assertEqual(v2, None)
        time.sleep(.01)
        self.tt.put('one', 4)
        time.sleep(.01)
        later = time.time()
        time.sleep(.01)
        self.tt.put('one', 5)
        time.sleep(.01)
        v3 = self.tt.get('one', later)
        self.assertEqual(v3, 4)




class BianaryTimeTravelTest(unittest.TestCase):
    def setUp(self):
        self.tt = ImprovedTraveler()

    def positive_test(self):
        early = time.time()
        time.sleep(.01)
        self.tt.put('one', 1)
        v = self.tt.get('one')
        self.assertEqual(v, 1)
        v2 = self.tt.get('one', early)
        self.assertEqual(v2, None)
        time.sleep(.01)
        self.tt.put('one', 4)
        time.sleep(.01)
        later = time.time()
        time.sleep(.01)
        self.tt.put('one', 5)
        time.sleep(.01)
        v3 = self.tt.get('one', later)
        self.assertEqual(v3, 4)
