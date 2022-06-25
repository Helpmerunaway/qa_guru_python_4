# Делаем списки!

l = ['string', 123, 2.5, ['another', 321]]

# разбивка на символы
#l = list('first')
print(l[0])
print(l[1: -1])


# Функции списков
# добавить
l.append('third')
# расширить
l.extend([1, 2, 2, 2, 3, 4])
# перевод в строку
l_string = str(l)
#
#assert l.count(2) == 3

# вставляет символ | между строками
print(' | '.join(['first', 'second', 'third']))

#print(", ".join([1, 2, 3]))
ll = ['first', 'second', 'third']
assert len(l) > 1, f"Длина слишком маленькая! " \
                     f"Элементы в списке: {', '.join(ll)}"

print(l)

# Множества
# множества включают в себя уникальные символы
s = set([1, 2, 3, 4 , 4, 5, 5, 5, 5])
ss = set([1, 2, 10])

print(s & ss)
print(s | ss)