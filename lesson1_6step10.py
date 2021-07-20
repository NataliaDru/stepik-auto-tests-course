from selenium import webdriver
# from selenium.webdriver.common.by import By
import time

try:
	link = "http://suninjuly.github.io/registration2.html"

	browser = webdriver.Chrome()
	browser.get(link)

	input1 = browser.find_element_by_css_selector(".first_block .first")
	input1.send_keys("Natalia")
	input2 = browser.find_element_by_css_selector(".first_block .second")
	input2.send_keys("Dru")
	input3 = browser.find_element_by_css_selector(".first_block .third")
	input3.send_keys("kek@gmail.com")
	
	button = browser.find_element_by_css_selector("button.btn")
	button.click()

	time.sleep(1)

	welcome_text_elt = browser.find_element_by_tag_name("h1")
	welcome_text = welcome_text_elt.text

	assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()