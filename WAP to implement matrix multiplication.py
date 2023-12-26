#29.WAP to implement matrix multiplication.
def matrix_multiplication(A, B):
  """
  This function multiplies two matrices A and B.

  Args:
    A: A 2D list representing the first matrix.
    B: A 2D list representing the second matrix.

  Returns:
    A 2D list representing the product of the two matrices.
  """

  if len(A[0]) != len(B):
    raise ValueError("Matrices cannot be multiplied.")

  result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
  for i in range(len(A)):
    for j in range(len(B[0])):
      for k in range(len(B)):
        result[i][j] += A[i][k] * B[k][j]

  return result


A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

print(matrix_multiplication(A, B))
