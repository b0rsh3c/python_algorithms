# 6.	Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

chars = 'abcdefghijklmnopqrstuvwxyz'
charindex = int(input('Введите номер буквы английского альфавита'))
char = chars[charindex-1]
print('Буква: {}'.format(char))