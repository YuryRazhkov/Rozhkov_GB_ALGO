# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

num_list = [5, 5, 1, 5, 2, 3, 6, 10, 5, 6]
a, b = sorted(num_list)[0:2]
print(a, b)