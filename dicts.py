# Заводим словарики (ключ - значение)
# словарь
d = {
     "key": "value",
     123: "another",
     10: {"another": "first"},
}

print(d["key"])

print(d.keys())
print(d.values())

# Функции словарей

print(d.get(123, ""))
print(list(d.items()))
# добавляем значение
d["first"] = "some string"

print(d)

value = d.pop("first")

print(value)