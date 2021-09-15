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
