""" For a given array of n integers, the function returns the index of the element with the minimum value in the array.
If there is more than one element with the minimum value, it returns the smallest one.
If an empty array is passed to the function, it raises an exception."""
def minimum_index(seq):
  if len(seq) == 0:
    raise ValueError('Cannot get the minimum value index from an empty sequence.')
  min_idx = 0
  for i in range(1, len(seq)):
    if seq[i] < seq[min_idx]:
      min_idx = i
  return min_idx

class TestDataEmptyArray(object):
  @staticmethod
  def get_array():
    # Complete this function
    return []

class TestDataUniqueValues(object):
  @staticmethod
  def get_array():
    # Complete this function
    return [1, 2, 3, 4, 5]

  @staticmethod
  def get_expected_result():
    # Complete this function
    return 0

class TestDataExactlyTwoDifferentMinimums(object):
  @staticmethod
  def get_array():
    # Complete this function
    return [1, 2, 3, 4, 5, 1]

  @staticmethod
  def get_expected_result():
    # Complete this function
    return 0

def TestWithEmptyArray():
  try:
    seq = TestDataEmptyArray.get_array()
    result = minimum_index(seq)
  except ValueError as e:
    pass
  else:
    assert False

def TestWithUniqueValues():
  seq = TestDataUniqueValues.get_array()
  assert len(seq) >= 2
  assert len(list(set(seq))) == len(seq)
  expected_result = TestDataUniqueValues.get_expected_result()
  result = minimum_index(seq)
  assert result == expected_result

def TestiWithExactyTwoDifferentMinimums():
  seq = TestDataExactlyTwoDifferentMinimums.get_array()
  assert len(seq) >= 2
  tmp = sorted(seq)
  assert tmp[0] == tmp[1] and (len(tmp) == 2 or tmp[1] < tmp[2])
  expected_result = TestDataExactlyTwoDifferentMinimums.get_expected_result()
  result = minimum_index(seq)
  assert result == expected_result

TestWithEmptyArray()
TestWithUniqueValues()
TestiWithExactyTwoDifferentMinimums()
print('OK!')
