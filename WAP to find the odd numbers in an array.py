#23.WAP to find the odd numbers in an array.
def find_odd_numbers(array):
  """Finds all the odd numbers in an array.

  Args:
    array: The array to search.

  Returns:
    A list of all the odd numbers in the array.
  """

  odd_numbers = []
  for number in array:
    if number % 2 != 0:
      odd_numbers.append(number)
  return odd_numbers


if __name__ == "__main__":
  array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  odd_numbers = find_odd_numbers(array)
  print(odd_numbers)
