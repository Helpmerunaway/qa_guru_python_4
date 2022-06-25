# Boolean
import random

t = True
f = False



# if/elif/else

if True:
	print("it's true!")

if False:
	print("It's false!")

if not False:
	print("It's false!")

if True and False:
	print("something")

b = True or False
if b:
	print("something123")

# 0 в питоне это False
if 0:
	print("zero")

# все кроме нуля это True
if 0:
	print("zero")

# False
if "":
	print("empty")

# True
if "123":
	print("empty")

# False
if None:
	print("None")

# 1 тру, 0 фальш
b = random.randint(0, 1)
if b:
	print('Got it!')
else:
	print("Nope")

# оператор сравнения
b = random.randint(0, 2)

if b == 0:
	print("Zero")
elif b ==1:
	print("One")
else:
	print("Something ele")

# либо через bool в python console
