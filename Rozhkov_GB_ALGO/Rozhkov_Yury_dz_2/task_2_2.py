# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры
# (4, 6 и 0) и 2 нечетные (3 и 5).

num = 34560

odd = 0
even = 0
for i in str(num):
    if int(i) % 2 == 0:
        even += 1
    else:
        odd += 1

print('even =', even, '\nodd =', odd)

