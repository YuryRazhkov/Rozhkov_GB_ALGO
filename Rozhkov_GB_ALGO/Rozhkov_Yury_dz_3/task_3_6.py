# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

num_list = [5, 5, 1, 5, 2, 3, 6, 10, 5, 6]
max_idx = num_list.index(max(num_list))
min_idx = num_list.index(min(num_list))

sum_el = 0
for i in range(min_idx+1, max_idx):
    sum_el += num_list[i]
print(sum_el)
