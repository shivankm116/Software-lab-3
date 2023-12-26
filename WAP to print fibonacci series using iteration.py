#32.WAP to print fibonacci series using iteration.
def fibonacci(n):
  """Prints the Fibonacci series up to the nth term."""
  a, b = 0, 1
  for i in range(n):
    print(a)
    a, b = b, a + b

if __name__ == '__main__':
  fibonacci(10)
