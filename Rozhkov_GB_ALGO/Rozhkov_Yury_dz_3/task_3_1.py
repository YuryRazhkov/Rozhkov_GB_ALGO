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
