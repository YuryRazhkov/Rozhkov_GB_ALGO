#4. Определить, какое число в массиве встречается чаще всего.

num_list = [56, 1, 1, 1, 1, 6413233, 2225, 411, 222, 2, 222222222, 4, 1, 6, 7, 2, 1, 5]
max_count = 0
dgt = 0
for i in num_list:
    if num_list.count(i) > max_count:
        max_count = num_list.count(i)
        dgt = i
print(dgt)
