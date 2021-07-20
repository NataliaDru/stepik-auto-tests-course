from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

link="http://suninjuly.github.io/explicit_wait2.html"

browser = webdriver.Chrome()
browser.get(link)

try:

	btn = WebDriverWait(browser, 12).until(
		EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

	btn = browser.find_element(By.ID, "book")
	btn.click()

	# page1 = browser.window_handles[0]
	# page2 = browser.window_handles[1]
	# browser.switch_to.window(page2)

	x = browser.find_element(By.ID, 'input_value')
	browser.execute_script("return arguments[0].scrollIntoView(true);", x)
	x = x.text
	x = calc(x)

	inp = browser.find_element(By.ID, 'answer')
	browser.execute_script("return arguments[0].scrollIntoView(true);", inp)
	inp.send_keys(x)

	btn2 = browser.find_element(By.ID, 'solve')
	browser.execute_script("return arguments[0].scrollIntoView(true);", btn2)
	btn2.click()

finally:
	time.sleep(10)
	browser.quit()
