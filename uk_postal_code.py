import re

def is_valid_uk_postal_code(postal_code):
  '''Validate if a string is a valid UK postal code. For the formats, A is a 
  letter and 9 is a digit. Returns True for the correct format with one or 
  no space in the middle. Whitespace on the beginning and end of the string
  is cleaned.'''

  # Check if argument is a string and that it is not an empty string
  if not isinstance(postal_code, str) or postal_code == '':
    return False

  # Transform the string in uppercase and remove spaces from start and end
  code_to_validate = postal_code.upper().strip()

  # The letters QVX are not used in the first position.
  if code_to_validate[0] in 'QVX':
    return False

  # The letters IJZ are not used in the second position.
  if code_to_validate[1] in 'IJZ':
    return False

  # The final two letters do not use the letters CIKMOV, so as not to resemble 
  # digits or each other when hand-written.
  if code_to_validate[-1] in 'CIKMOV' or code_to_validate[-2] in 'CIKMOV':
    return False

  # Check for format AA9A 9AA
  if (re.match(r'^[A-Z][A-Z]\d[A-Z]\s\d[A-Z][A-Z]$', code_to_validate) or
    re.match(r'^[A-Z][A-Z]\d[A-Z]\d[A-Z][A-Z]$', code_to_validate)):
    # The only letters to appear in the fourth position are ABEHMNPRVWXY when 
    # the structure starts with AA9A.
    if code_to_validate[3] not in 'ABEHMNPRVWXY':
      return False
    else:
      return True
  
  # Check for format A9A 9AA
  if (re.match(r'^[A-Z]\d[A-Z]\s\d[A-Z][A-Z]$', code_to_validate) or
    re.match(r'^[A-Z]\d[A-Z]\d[A-Z][A-Z]$', code_to_validate)):
    # The only letters to appear in the third position are ABCDEFGHJKPSTUW 
    # when the structure starts with A9A.
    if code_to_validate[2] not in 'ABCDEFGHJKPSTUW':
      return False
    else:
      return True

  # Check for format A9 9AA
  if (re.match(r'^[A-Z]\d\s\d[A-Z][A-Z]$', code_to_validate) or
    re.match(r'^[A-Z]\d\d[A-Z][A-Z]$', code_to_validate)):
    return True

  # Check for format A99 9AA
  if (re.match(r'^[A-Z]\d\d\s\d[A-Z][A-Z]$', code_to_validate) or
    re.match(r'^[A-Z]\d\d\d[A-Z][A-Z]$', code_to_validate)):
    return True

  # Check for format AA9 9AA
  if (re.match(r'^[A-Z][A-Z]\d\s\d[A-Z][A-Z]$', code_to_validate) or
    re.match(r'^[A-Z][A-Z]\d\d[A-Z][A-Z]$', code_to_validate)):
    return True

  # Check for format AA99 9AA
  if (re.match(r'^[A-Z][A-Z]\d\d\s\d[A-Z][A-Z]$', code_to_validate) or
    re.match(r'^[A-Z][A-Z]\d\d\d[A-Z][A-Z]$', code_to_validate)):
    return True

  # If there is no check, Return False
  return False

def format_uk_postal_code(postal_code):
  '''Check if a postal code is valid and then format it, inserting the space 
  if necessary'''

  # Check if it is a valid postal code
  if not is_valid_uk_postal_code(postal_code):
    return None

  # Transform the string in uppercase and remove spaces from start and end
  code_to_format = postal_code.upper().strip()  

  # Check if there is no space in the middle of the string
  if len(code_to_format.replace(" ","")) == len(code_to_format):
    # If there is not, insert the space before the 3 final characters
    formatted_code = code_to_format[:len(code_to_format)-3] + " " + code_to_format[len(code_to_format)-3:]
  else:
    # If there is, keep the string as it is
    formatted_code = code_to_format

  # Return the formatted code
  return formatted_code