import unittest
from print_1_to_100 import print_1_to_100_scurri

from contextlib import contextmanager
from io import StringIO
import sys


@contextmanager
def captured_output():
  '''Function used to capture the output, which will be used for testing 
  since the function does not have a return value'''
  new_out, new_err = StringIO(), StringIO()
  old_out, old_err = sys.stdout, sys.stderr
  try:
    sys.stdout, sys.stderr = new_out, new_err
    yield sys.stdout, sys.stderr
  finally:
    sys.stdout, sys.stderr = old_out, old_err

class TestPrint1To100(unittest.TestCase):
  def setUp(self):
    # Capture the output of the function
    with captured_output() as (out, err):
      print_1_to_100_scurri()
    
    self.output = out.getvalue().strip()

  # Test if the function outputs 100 lines
  def test_number_of_lines(self):
    self.assertEqual(len(self.output.split('\n')), 100)

  # Test if the first element printed is a "1"
  def test_first_element(self):
    self.assertEqual(self.output.split('\n')[0], "1")

  # Test if the last element is a "five"
  def test_last_element(self):
    self.assertEqual(self.output.split('\n')[-1], "Five")

if __name__ == '__main__':
  unittest.main()