# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

matrix = [[4, 5, 5, 4, 18],
          [8, 9, 9, 5, 31],
          [2, 4, 8, 1, 15],
          [5, 5, 1, 2, 13]]
result = []
for i in range(len(matrix)):
    a = min(matrix[i])
    result.append(a)
print(result)
