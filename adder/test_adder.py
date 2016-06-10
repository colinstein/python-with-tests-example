import unittest
from . import *

class TestAdder(unittest.TestCase):

  def testIntegers(self):
    self.assertEqual(3, adder.addI(1, 2))

  def testIntegerString(self):
    self.assertEqual(14, adder.addI("7", 7))

  def testStrings(self):
    self.assertEqual(579, adder.addI("123", "456"))

  def testNegativeIntegers(self):
    self.assertEqual(-3, adder.addI(-1, -2))

  def testNegativeStrings(self):
    self.assertEqual(-35, adder.addI("-27", "-8"))

  def testFloats(self):
    self.assertEqual(11, adder.addI( 7.7, 4.1))

  def testStringsFail(self):
    self.assertRaises(ValueError, adder.addI, "Hello", "world")
