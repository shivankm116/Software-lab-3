#30.WAP to check leap year.
def is_leap_year(year):
  """Returns True if the given year is a leap year, False otherwise."""
  return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def main():
  """Prompts the user for a year and prints whether it is a leap year."""
  year = int(input("Enter a year: "))
  if is_leap_year(year):
    print(f"{year} is a leap year.")
  else:
    print(f"{year} is not a leap year.")


if __name__ == "__main__":
  main()
