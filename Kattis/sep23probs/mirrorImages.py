import sys

def reverse_matrix(matrix):
    reverse = []
    matrix_rows = len(matrix)
    matrix_cols = len(matrix[0])
    for row in range(matrix_rows):
        for col in range(matrix_cols):
            reverse[row][col] = matrix[matrix_rows-row][matrix_cols-col]
    return reverse

for test in sys.stdin:
    test_count = int(test)
    i = 0
    while i < test_count:
        for matrix_size in sys.stdin:
            matrix = []
            rows, cols = [int(i) for i in matrix_size.strip().split()]
            j = 0
            for row in sys.stdin:
                if j >= rows:
                    break
                matrix.append(row)
                j += 1
                    
            reverse = reverse_matrix(matrix)
            print(f'Test {i}')
            print(reverse)

        i += 1
    if test_count == i:
        break

