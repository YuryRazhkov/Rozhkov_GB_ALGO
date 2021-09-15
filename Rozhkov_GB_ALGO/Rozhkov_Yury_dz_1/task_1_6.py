#6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.


a = int(input('number of letter: '))
print(f'"{chr(ord("a")+a-1)}" is your letter')
