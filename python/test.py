#!/usr/bin/env python3

import unittest

from get_counter import *
from return_spam_line import *

class TestCounter(unittest.TestCase):

    def test_get_counter0(self):
        self.assertEqual(get_counter("2022-01-01 00:00"), 0)
    def test_create_counter0(self):
        self.create_test = create_counter("2022-01-01 00:00")
    def test_increment_counter1(self):
        self.increment_test = increment_counter("2022-01-01 00:00")
    def test_get_counter1(self):
        self.assertEqual(get_counter("2022-01-01 00:00"), 1)
    def test_increment_counter2(self):
        self.increment_test = increment_counter("2022-01-01 00:00")
    def test_get_counter2(self):
        self.assertEqual(get_counter("2022-01-01 00:00"), 2)

    def test_return_spam0(self):
        self.assertEqual(return_spam_line(0), "Egg and Spam")
    def test_return_spam1(self):
        self.assertEqual(return_spam_line(1), "Egg, bacon and Spam")
    def test_return_spam8(self):
        self.assertEqual(return_spam_line(8), "Spam, Spam, Spam, Spam, Spam, Spam, Spam and Spam")

if __name__ == '__main__':
    unittest.main()