import os
from selenium import webdriver
import time

link="http://suninjuly.github.io/file_input.html"

try:
	browser = webdriver.Chrome()
	browser.get(link)

	input1 = browser.find_element_by_css_selector('input[name="firstname"]')
	input1.send_keys('Natalia')

	input2 = browser.find_element_by_css_selector('input[name="lastname"]')
	input2.send_keys('Ginger')

	input3 = browser.find_element_by_css_selector('input[name="email"]')
	input3.send_keys('lol@mail.ru')

	current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
	file_path = os.path.join(current_dir, 'test_file.txt')           # добавляем к этому пути имя файла 
	element = browser.find_element_by_css_selector('input[name="file"]')
	# element.click()
	element.send_keys(file_path)

	button = browser.find_element_by_css_selector('button.btn.btn-primary')
	button.click()
finally:
	time.sleep(10)
	browser.quit()

print(os.path.abspath(__file__))
print(os.path.abspath(os.path.dirname(__file__)))