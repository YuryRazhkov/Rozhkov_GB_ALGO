#5. Пользователь вводит две буквы. Определить,
# на каких местах алфавита они стоят и сколько между ними находится букв.

a = input('letter from: ')
b = input('letter to: ')
print(f'{a} is on position #{ord(a) - ord("a") + 1}, {b} is on position #{ord(b) - ord("a") + 1}')
print(f'{(ord(b) - ord("a") + 1) - (ord(a) - ord("a") + 1)} letters between {a} and {b}')
