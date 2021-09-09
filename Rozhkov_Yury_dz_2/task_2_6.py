# 6. В программе генерируется случайное целое число от 0 до 100. Пользователь
# должен его отгадать не более чем за 10 попыток. После каждой неудачной попытки
# должно сообщаться больше или меньше введенное пользователем
# число, чем то, что загадано. Если за 10 попыток число не отгадано, то вывести загаданное число.

from random import randint

x = randint(1, 100)
for i in range(10):
    y = int(input('enter your number :'))
    if y > x:
        print(y, "bigger then x. attempts left:", 9-i)
    elif y < x:
        print(y, "smaller then then x. attempts left:", 9-i)
    else:
        print('you win!')
        break
    if i == 9:
        print('you lose!')
print('x =',x)