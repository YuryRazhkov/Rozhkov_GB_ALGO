# 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

#8.1

num = input('Количество вводимых чисел последовательности: ')
dgt = input('Искомая цифра от 0 до 9: ')
num_total = ''
for i in range(int(num)):
    num_total += input('введите число последовательности')
print(f'в последовательности чисел {num_total} цифра {dgt} встречается {num_total.count(dgt)} раз')

#8.2. Но тут количество вводимых чисел последовательности не задаются с клавиатуры

num = input('enter your number: ')
dgt = input('enter your digit to count: ')
print(num.count(dgt))