@ -0,0 +1,14 @@
# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из
# них кратны каждому из чисел в диапазоне от 2 до 9.

result = {}
for i in range(2, 10):
    sum = 0
    for a in range(2, 100):
        if a % i == 0:
            sum += 1
            result[i] = sum

print(result)

# 2. Во втором массиве сохранить индексы четных элементов первого массива.
# например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то
# во второй массив надо заполнить значениями 1, 4, 5, 6
# (или 0, 3, 4, 5 - если индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.

first_list = [8, 3, 15, 6, 4, 2]
second_list = []

for i in range(len(first_list)):
    if first_list[i] % 2 == 0:
        second_list.append(i)

print(second_list)


# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

# при реализации исходил из предположения, что меняться должен прежний массив,
# и новый массив создавать нельзя.

list = [56, 1, 6413233, 2225, 411, 2222222222222, 4]
max_idx = list.index(max(list))
min_idx = list.index(min(list))
max_value = max(list)
min_value = min(list)
list[max_idx] = min_value
list[min_idx] = max_value

print(list)


#4. Определить, какое число в массиве встречается чаще всего.

num_list = [56, 1, 1, 1, 1, 6413233, 2225, 411, 222, 2, 222222222, 4, 1, 6, 7, 2, 1, 5]
max_count = 0
dgt = 0
for i in num_list:
    if num_list.count(i) > max_count:
        max_count = num_list.count(i)
        dgt = i
print(dgt)

+# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

num_list = [56, -1, 1, 1, 1, 6413233, -2225, 411, -222, 2, 222222222, -4, 1, 6, 7, 2, 1, 5]

min_el = 0
pose_el = 0
for i in range(len(num_list)):
    if num_list[i] < min_el:
        min_el = num_list[i]
        pose_el = i

print(f'min element is {min_el} on position {pose_el}')

# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

num_list = [5, 5, 1, 5, 2, 3, 6, 10, 5, 6]
max_idx = num_list.index(max(num_list))
min_idx = num_list.index(min(num_list))

sum_el = 0
for i in range(min_idx+1, max_idx):
    sum_el += num_list[i]
print(sum_el)


+# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

num_list = [5, 5, 1, 5, 2, 3, 6, 10, 5, 6]
a, b = sorted(num_list)[0:2]
print(a, b)

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