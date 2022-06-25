# Списки словари и множества - изменяемые!
import copy
from copy import deepcopy


l = [1, 2, 3, [4, 5, 6]]
ll = l
# присвоение
#ll[3].append(4)
# это множество
#d = {"key", "value", "some": {"first": 1}}
# это словарь
d = {"key":"value", "some": {"first": 1}}

dd = d.copy()

dd['second'] = 2
s = set()

# d = {}
# s = set()


# Кортежи, frozenset - нет

# кортеж = неизменяемый список = (tuple)

t = (1, 2, 3, 4, 5)
tt = t
print()

s = set()

f_s = frozenset()
