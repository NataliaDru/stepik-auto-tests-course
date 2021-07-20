from selenium import webdriver
import time
#import math

#def calc(x):
#	return str(math.log(abs(12*math.sin(int(x)))))

link="http://suninjuly.github.io/cats.html"

browser = webdriver.Chrome()
browser.get(link)

try:
	browser.execute_script("alert('Robots at work');")
	
	#btn1 = browser.find_element_by_css_selector("button.trollface.btn.btn-primary")
	#btn1.click()

	#page1 = browser.window_handles[0]
	#page2 = browser.window_handles[1]
	#browser.switch_to.window(page2)

	#x = browser.find_element_by_css_selector('#input_value')
	#x = x.text
	#x = calc(x)

	#inp = browser.find_element_by_css_selector('input#answer')
	#inp.send_keys(x)

	#btn2 = browser.find_element_by_css_selector('button.btn.btn-primary')
	#btn2.click()

finally:
	time.sleep(10)
	browser.quit()
