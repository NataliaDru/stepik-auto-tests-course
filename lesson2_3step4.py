from selenium import webdriver
import time
import math

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))


link="http://suninjuly.github.io/alert_accept.html"

try:
	browser = webdriver.Chrome()
	browser.get(link)

	btn1 = browser.find_element_by_css_selector('button.btn.btn-primary')
	btn1.click()

	alert1 = browser.switch_to.alert
	alert1.accept()

	x = browser.find_element_by_css_selector('#input_value')
	x = x.text
	x = calc(x)

	inp = browser.find_element_by_css_selector('input#answer')
	inp.send_keys(x)

	btn2 = browser.find_element_by_css_selector('button.btn.btn-primary')
	btn2.click()

finally:
	time.sleep(10)
	browser.quit()