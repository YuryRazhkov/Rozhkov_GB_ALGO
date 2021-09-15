# 8. Определить, является ли год, который ввел пользователем, високосным или невисокосным.


y = int(input('enter year: '))
if y % 400 == 0 or y % 100 != 0 and y % 4 == 0:
    print(str(y), 'is leap year')
else:
    print(str(y), 'is not leap year')
