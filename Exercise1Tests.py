from exercise1 import findNext
import unittest

class Exercise1Tests(unittest.TestCase):
    def test_nextval(self):
        self.assertEqual(findNext('1234'),'1243')
        self.assertEqual(findNext('250'),'502')
        self.assertEqual(findNext('580'),'805')
        self.assertEqual(findNext('13542'),'14235')
        self.assertEqual(findNext('218765'),'251678')
        self.assertEqual(findNext('534976'),'536479')
        self.assertEqual(findNext('38276'),'38627')

    def test_nextval_int_input(self):
        self.assertEqual(findNext(13642),'14236')

    def test_raise_value_error(self):
        with self.assertRaises(ValueError):
            findNext('abcd')

unittest.main()