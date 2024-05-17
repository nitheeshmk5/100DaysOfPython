from bs4 import BeautifulSoup
import requests
import lxml
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


res = requests.get(url='https://appbrewery.github.io/Zillow-Clone/')
contents = res.text

soup = BeautifulSoup(contents,'lxml')

houses_amt_list = soup.find_all(name='span',class_='PropertyCardWrapper__StyledPriceLine')
houses_amt = [names.getText().strip('+/mo') for names in houses_amt_list]

#address_list = soup.find_all()
link_list = soup.find_all(name='a',class_='StyledPropertyCardDataArea-anchor')
address = [l.getText().strip('\n').strip() for l in link_list]

links = []

for link in soup.find_all('a', href=True,class_='StyledPropertyCardDataArea-anchor'):
    links.append(link['href'])

# print(len(links))
# print(len(houses_amt))


## SUBMITING FORM
options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=options)
driver.get('https://forms.gle/FPUbFG4Lb7CofzJq7')

for i in range(len(houses_amt)):
    address_element = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div[2]/textarea')
    address_element.send_keys(address[i])

    amt_element = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    amt_element.send_keys(houses_amt[i])

    link_element = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_element.send_keys(links[i])

    submit_element = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit_element.click()

    submit_again = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    submit_again.click()

#amt_element = driver.find_element(By.CLASS_NAME,'KHxj8b')