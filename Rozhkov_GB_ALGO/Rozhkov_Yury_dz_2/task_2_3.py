# 3. Сформировать из введенного числа
# обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, то надо вывести число 6843.

a = input('enter your number: ')

# 3.1 Простой срез
print(a[::-1])

# 3.2 С использованием цикла и строковых методов
result = ''
for i in range(1, len(a)+1):
    result += str(a[-i])
    i += 1
print(result)

# 3.3 С использованием цикла и деления
result = 0
a_int = int(a)
for i in range(1, len(a)+1):
    x = (a_int % 10)*10**(len(a)-i)
    a_int //= 10
    result += x
print(result)
