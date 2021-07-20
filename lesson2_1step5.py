from selenium import webdriver
import math
import time

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

link="http://suninjuly.github.io/math.html"

try:
	browser = webdriver.Chrome()
	browser.get(link)

	x_element = browser.find_element_by_css_selector("#input_value")
	x = x_element.text
	y = calc(x)

	input1 = browser.find_element_by_css_selector("#answer")
	input1.send_keys(y)

	checkbox1 = browser.find_element_by_css_selector("#robotCheckbox")
	checkbox1.click()

	radio1 = browser.find_element_by_css_selector("#robotsRule")
	radio1.click()

	button = browser.find_element_by_css_selector(".btn.btn-default")
	button.click()


finally:
	time.sleep(10)
	browser.quit()

