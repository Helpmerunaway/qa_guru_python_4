from inspect import getfullargspec


def get_func_info(func):
	name = func.__name__
	arguments = getfullargspec(func)
	print(f"Имя функции: {name}. Аргументы функции: {arguments[0]}")


def open_browser(browser_name):
	pass


def go_to_companyname_homepage(page_url):
	pass


def find_registration_button_on_login_page(page_url, button_text):
	pass


functions = [open_browser, go_to_companyname_homepage, find_registration_button_on_login_page]


for func in functions:
	get_func_info(func)
