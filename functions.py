# Обьявляем функции

def func(arg1, arg2, arg3='third'):
	print(arg1, arg2, arg3)

func("hello!", 123, "321")

def upper_string(string: str):
	return string.upper()

print(upper_string("some lowercase"))



# Переменное количество аргументов

# передаем аргументы
print('\n==================')
def print_all_arguments(*args, end="\n"):
	for arg in args:
		print(arg, end=end)

def print_all_arguments_v2(*args, end="\n"):
	print(*args, end=end)

print_all_arguments(2, 3, 4, 5, 6, 7, 8, end="")
print()
print_all_arguments_v2(3, 4, 5, 6, 7, 8, end="")



#  имя = значение
def print_pairs(**kwargs):
	settings = kwargs.pop("settings")
	for key, value in kwargs.items():
		print(key, value)

print_pairs(key='value', some='another', etc=321, settings="fafafa")

d = {"first": 1}
dd = {"second": 2}
# запихивает из первого во второй
d.update()

ddd = {**d, **dd}
print(ddd)

def f():
	return 1, 2, 3

# cписок
a, b, c = f()
# кортеж
#a = f()
print(a, b, c)

# Функции - тоже обьект

# полезная штука при сортировке списка
f = lambda x: x + 1

def func():
	pass

my_super_function = func