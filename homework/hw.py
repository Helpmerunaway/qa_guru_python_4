# Сделайте функцию, которая будет печатать
# читаемое имя переданной ей функции и ее аргументов.
# Вызовите ее для трех функций ниже в цикле
# Подсказка: Имя функции можно получить с помощью func.__name__


def open_browser(browser_name):
    pass

func1 = open_browser.__name__

def go_to_companyname_homepage(page_url):
    pass

func2 = go_to_companyname_homepage.__name__

def find_registration_button_on_login_page(page_url, button_text):
    pass

func3 = find_registration_button_on_login_page.__name__


functions = [open_browser, go_to_companyname_homepage, find_registration_button_on_login_page]



def get_function_name(func):
	for functions in func:
		print('Function name', functions.__name__)
		if not any(functions.__name__):
			print('Nothing there')
		else:
			print(functions)
print(func1, func2, func3, sep=" | ")