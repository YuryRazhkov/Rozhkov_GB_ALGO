# 8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

mtrx = []

for i in range(4):
    mtrx += [list(input('enter 4 digits:'))]
    mtrx[i] = ([int(item) for item in mtrx[i]])
    mtrx[i].append(sum(mtrx[i]))
    if i < 3:
        print('current matrix', mtrx)
print('final matrix', mtrx)
