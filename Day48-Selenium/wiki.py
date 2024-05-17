from selenium import webdriver
from selenium.webdriver.common.by import By


web_options = webdriver.ChromeOptions()
web_options.add_experimental_option('detach',True)


driver = webdriver.Chrome(options=web_options)
driver.get('https://en.wikipedia.org/wiki/Main_Page')

price = driver.find_element(By.CSS_SELECTOR,'#articlecount a')

print(price.text)