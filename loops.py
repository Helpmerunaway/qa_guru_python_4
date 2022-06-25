# While

# цикл по цифрам
i = 8
while i < 10:
	print("something" + str(i))
	i += 1


# For
# цикл по спискам
l = ['first', 'second', 'third']

for element in l:
	print(element)

for element in "this is string":
	print(element, end="")

print("\n==============")

from dicts import d

print("\n==============")

# итерируемся по словарям

for key, item in d.items():
	print(key, item, sep=" | ")


l = ['first', 'second', 'third']

# range - функция дает диапазон чисел, например тут от 0 до 9 (от 0 если
# не указано другое, шаг 1 по умолчанию)
for i in range(10):
	print(i)

print('\n==============')

l = ['first', 'second', 'third']

for i in range(3, len(l)):
	print(l[i])

# язык С
# for (int i = 1; i < 10; i++)