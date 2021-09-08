#4. Написать программу, которая генерирует в указанных пользователем границах:
# случайное целое число;
# случайное вещественное число;
# случайный символ.

from random import uniform, randint

print('random int')
a = int(input('digit from: '))
b = int(input('digit to: '))
print(randint(a, b), '- random int', end='\n\n')

print('random float')
a = float(input('digit from: '))
b = float(input('digit to: '))
print(uniform(a, b), '- random float', end='\n\n')

print('random symbol1')
a = input('letter from: ')
b = input('letter to: ')
print(chr(randint(ord(a), ord(b))), '- random symbol', end='\n\n')
