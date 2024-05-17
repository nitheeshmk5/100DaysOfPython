from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


web_options = webdriver.ChromeOptions()
web_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=web_options)
driver.get('http://secure-retreat-92358.herokuapp.com/')

first_name = driver.find_element(By.NAME, value="fName")
last_name =  driver.find_element(By.NAME, value="lName")
email =  driver.find_element(By.NAME, value="email")


first_name.send_keys("Nitheesh")
last_name.send_keys("Muthu Krishnan C")
email.send_keys("info@nitheeshmk.in" ,Keys.ENTER)

