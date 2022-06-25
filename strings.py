# Учимся писать строки!

s = 'i am a "teapot!"'

s = "i am a 'teapot!'"

s = 'i am a \teapot\!'

s = """i am a teapot!"""

s = '''i am a teapot!'''

multiline_string = "first" \
                   "second" \
                   "third"
print(multiline_string)

multiline_string = """first
second
third"""
print(multiline_string)

multiline_string = "first\n" \
                   "second\n" \
                   "third"

print(multiline_string)

print('this is stri\\ng')

print(r'this is stri\ng')

# Индексы и слайсы

s = 'abcdefg'
print(s[0])
print(s[1])
print(type(s))
print(type(s[0]))

print(s[: -1])
# 0 - начало, 3 конец строки
print(s[0: 3])

print(s[0:-1:2])

# реверс строки
print(s[::-1])

# Оперируем

print("hello, world!".replace("hello", 'bye'))
# замена
print('hello world'.replace("o", "0"))
# список
print('hello, world!'.split())

# проверка начинается ли строка со слова hello
assert "hello, world".startswith("hello")

# assert "hello, world".startswith("bye")

# оканчивается ли строка со слова world
assert "hello, world".endswith('world')
# делает большой первую букву
print('hello, world'.capitalize())
# капс
print('hello, world'.upper())
# маленькие
print('hello, world'.lower())
# первая буква большая у каждого слова
print('hello, world'.title())

# Форматируем

first = 'first'
second = 'second'
third = 'third'

print("fa" "fa" "fa")
# сложение переменных
print(first + " " + second + " " + third +" ")
print(first, second, third)
# f строка с 3.6
print(f'{first} {second} {third}')

print(f'{first} {second} {third.title()}{3 + 5}')

print(f'{first} {second} {third.title()}{100}')
# старый метод форматирование строки
print("{2} {1} {0}".format(first, second, third.title()))
# пример где применяется старый метод
# logging.log("{2} {1} {0}")
# способ форматирования строк (еще старее)
print("%s %s %s" % (first, second, third.title()))

#print(100 + '100')
print(100 + int('100'))

s = '100'
print(100 + int(s))

s = '(100)'
s = s.replace("(","").replace(")(",)
# проверяем что строка это число
assert s.isdigit()

print(1000 + int(s))