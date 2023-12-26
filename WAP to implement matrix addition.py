#28.WAP to implement matrix addition.
def add_matrices(matrix1, matrix2):
  """Adds two matrices together.

  Args:
    matrix1: A 2D list representing the first matrix.
    matrix2: A 2D list representing the second matrix.

  Returns:
    A 2D list representing the sum of the two matrices.
  """

  if len(matrix1) != len(matrix2):
    raise ValueError("Matrices must have the same number of rows.")
  if len(matrix1[0]) != len(matrix2[0]):
    raise ValueError("Matrices must have the same number of columns.")

  result = [[0 for _ in range(len(matrix1[0]))] for _ in range(len(matrix1))]
  for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
      result[i][j] = matrix1[i][j] + matrix2[i][j]
  return result


matrix1 = [[1, 2], [3, 4]]
matrix2 = [[5, 6], [7, 8]]
print(add_matrices(matrix1, matrix2))
