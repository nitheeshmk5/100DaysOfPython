from selenium import webdriver
from selenium.webdriver.common.by import By

web_options = webdriver.ChromeOptions()
web_options.add_experimental_option("detach",True)

driver = webdriver.Chrome()
driver.get('https://www.python.org')

events_times = driver.find_elements(By.CSS_SELECTOR,'.event-widget time')
events_names = driver.find_elements(By.CSS_SELECTOR,'.event-widget li a')

events = {}

for i in range(len(events_times)):
    events[i] = {
        events_names[i].text :events_times[i].text
    }

print(events)