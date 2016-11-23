import unittest
from uk_postal_code import is_valid_uk_postal_code, format_uk_postal_code


class TestUKPostalCodeValidator(unittest.TestCase):
  '''Tests for the UK Postal Code Validator'''
  def setUp(self):
    pass

  # Test a valid input for each accepted format
  def test_valid_postal_code_format_AA9A_9AA(self):
    self.assertTrue(is_valid_uk_postal_code('EC1A 1BB'))
    self.assertTrue(is_valid_uk_postal_code('EC1A1BB'))

  def test_valid_postal_code_format_A9A_9AA(self):
    self.assertTrue(is_valid_uk_postal_code('W1A 0AX'))
    self.assertTrue(is_valid_uk_postal_code('W1A0AX'))

  def test_valid_postal_code_format_A9_9AA(self):
    self.assertTrue(is_valid_uk_postal_code('M1 1AE'))
    self.assertTrue(is_valid_uk_postal_code('M11AE'))

  def test_valid_postal_code_format_A99_9AA(self):
    self.assertTrue(is_valid_uk_postal_code('B33 8TH'))
    self.assertTrue(is_valid_uk_postal_code('B338TH'))

  def test_valid_postal_code_format_AA9_9AA(self):
    self.assertTrue(is_valid_uk_postal_code('CR2 6XH'))
    self.assertTrue(is_valid_uk_postal_code('CR26XH'))

  def test_valid_postal_code_format_AA99_9AA(self):
    self.assertTrue(is_valid_uk_postal_code('DN55 1PT'))
    self.assertTrue(is_valid_uk_postal_code('DN551PT'))

  # Test with invalid postal codes
  def test_invalid_postal_code(self):
    self.assertFalse(is_valid_uk_postal_code('DN55 1PTAAA'))
    self.assertFalse(is_valid_uk_postal_code('EC1A     1BB'))    
    self.assertFalse(is_valid_uk_postal_code(1234))
    self.assertFalse(is_valid_uk_postal_code('EC1A 1BM'))
    self.assertFalse(is_valid_uk_postal_code('W1L 0AX'))
    self.assertFalse(is_valid_uk_postal_code('QC1A 1BB'))
    self.assertFalse(is_valid_uk_postal_code('EJ1A 1BB'))
    

  # Test with an empty string
  def test_empty_string(self):
    self.assertFalse(is_valid_uk_postal_code(''))

class TestFormatUKPostalCode(unittest.TestCase):
  '''Test for the formatting function'''
  def setUp(self):
    pass

  # Test formatting function with valid postal codes in different formats
  def test_format_with_valid_postal_code(self):
    self.assertEqual(format_uk_postal_code('EC1A 1BB'), 'EC1A 1BB')
    self.assertEqual(format_uk_postal_code('EC1A1BB'), 'EC1A 1BB')
    self.assertEqual(format_uk_postal_code('ec1a 1bb'), 'EC1A 1BB')
    self.assertEqual(format_uk_postal_code('CR2 6XH'), 'CR2 6XH')
    self.assertEqual(format_uk_postal_code('CR26XH'), 'CR2 6XH')
    self.assertEqual(format_uk_postal_code('M1 1AE'), 'M1 1AE')
    self.assertEqual(format_uk_postal_code('M11AE'), 'M1 1AE')

  # Test formatting function with invalid postal codes
  def test_format_with_invalid_postal_code(self):
    self.assertIsNone(format_uk_postal_code('AAAAAA'))    
    self.assertIsNone(format_uk_postal_code(1234))
    self.assertIsNone(format_uk_postal_code('EC1A        1BB'))

  # Test formatting function with an empty string
  def test_format_with_empty_string(self):
    self.assertIsNone(format_uk_postal_code(''))

if __name__ == '__main__':
  unittest.main()