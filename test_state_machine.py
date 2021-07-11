#!/usr/bin/env python3
import unittest
from state_machine import *

class TestStateMachine(unittest.TestCase):
    def test_accumulator_step(self):
        a = Accumulator()
        self.assertEqual(a.step(1), 1)
        self.assertEqual(a.step(2), 3)
        self.assertEqual(a.step(-5), -2)

    def test_accumulator_transduce(self):
        a = Accumulator()
        self.assertEqual(a.transduce([100, -3, 4, -123, 10]), [100, 97, 101, -22, -12])

    def test_updown_step(self):
        ud = UpDown()
        self.assertEqual(ud.step("u"), 1)
        self.assertEqual(ud.step("u"), 2)
        self.assertEqual(ud.step("d"), 1)

    def test_updown_transduce(self):
        ud = UpDown()
        self.assertEqual(ud.transduce(list("uuuddu")), [1, 2, 3, 2, 1, 2])

    def test_delay_step(self):
        d = Delay(-9)
        self.assertEqual(d.step(2), -9)
        self.assertEqual(d.step(3), 2)
        self.assertEqual(d.step(4), 3)

    def test_delay_transduce(self):
        d = Delay(1)
        self.assertEqual(d.transduce([7, 2, -4, 5, 4]), [1, 7, 2, -4, 5])

    def test_avg2_step(self):
        avg = Average2()
        self.assertEqual(avg.step(5), 2.5)
        self.assertEqual(avg.step(-4), 0.5)

    def test_avg2_transduce(self):
        avg = Average2()
        self.assertEqual(avg.transduce([10, 5, 2, 10]), [5, 7.5, 3.5, 6])

    def test_sum3_step(self):
        sum = Sum3()
        self.assertEqual(sum.step(5), 5)
        self.assertEqual(sum.step(-4), 1)

    def test_sum3_transduce(self):
        sum = Sum3()
        self.assertEqual(sum.transduce([2, 1, 3, 4, 10, 1, 2, 1, 5]), [2, 3, 6, 8, 17, 15, 13, 4, 8])

if __name__ == "__main__":
    unittest.main()
