#27.WAP to check whether a string is palindrome or not.
def is_palindrome(string):
  """
  Checks if a string is a palindrome.

  A palindrome is a string that reads the same backwards as forwards.

  Args:
    string: The string to check.

  Returns:
    True if the string is a palindrome, False otherwise.
  """

  string = string.lower()
  string = string.replace(" ", "")

  return string == string[::-1]


if __name__ == "__main__":
  string = input("Enter a string: ")

  if is_palindrome(string):
    print(f"{string} is a palindrome.")
  else:
    print(f"{string} is not a palindrome.")
