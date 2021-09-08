# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

nums = (input('числа через пробел: ')).split()
nums_sum = {}
for i in nums:
    sum_el = 0
    for el in i:
        sum_el += int(el)
    nums_sum[i] = sum_el
max_num, max_sum = (max((key, value) for key, value in nums_sum.items()))
print(f'число {max_num} c суммой цифр {max_sum}')