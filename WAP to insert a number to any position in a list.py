#25.WAP to insert a number to any position in a list.
def insert_number_to_list(list1, number, position):
  """Inserts a number to any position in a list.

  Args:
    list1: The list to insert the number into.
    number: The number to insert.
    position: The position to insert the number at.
  """

  # Check if the position is valid.
  if position < 0 or position > len(list1):
    raise ValueError("Invalid position.")

  # Insert the number into the list.
  list1.insert(position, number)

  # Return the list.
  return list1


# Example usage:
list1 = [1, 2, 3, 4, 5]
number = 6
position = 2

list1 = insert_number_to_list(list1, number, position)

print(list1)
