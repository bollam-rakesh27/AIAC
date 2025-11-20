def matrix_multiply(matrix_a, matrix_b):
    """
    Multiply two matrices and return the result.  
    Args:
        matrix_a: List of lists representing the first matrix (m x n)
        matrix_b: List of lists representing the second matrix (n x p)  
    Returns:
        List of lists representing the result matrix (m x p)
 """
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    rows_b = len(matrix_b)
    cols_b = len(matrix_b[0])
    if cols_a != rows_b:
        raise ValueError("Number of columns in matrix_a must equal number of rows in matrix_b")
    result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]
    
    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j] 
    return result

# Example usage
if __name__ == "__main__":
    a = [[1, 2, 3],
         [4, 5, 6]]
    
    b = [[7, 8],
         [9, 10],
         [11, 12]]
    
    result = matrix_multiply(a, b)
    
    for row in result:
        print(row)