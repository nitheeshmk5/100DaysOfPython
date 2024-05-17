from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import time
from dotenv import load_dotenv


load_dotenv()

TWITTER_EMAIL = os.getenv('X_MAIL')
TWITTER_PASSWORD = os.getenv('X_PASS')


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)

# Function to get internet speed
def get_internet_speed():
    driver.get('https://www.speedtest.net/')
    time.sleep(5)

    # Attempt to close the cookie consent pop-up if it exists
    try:
        driver.find_element(By.ID, 'onetrust-accept-btn-handler').click()
        time.sleep(2)
    except:
        pass

    # Click the start button
    driver.find_element(By.CLASS_NAME, 'start-text').click()

    time.sleep(50)

    download_speed = driver.find_element(By.CLASS_NAME, 'download-speed').text
    upload_speed = driver.find_element(By.CLASS_NAME, 'upload-speed').text

    print(f"Download speed: {download_speed} Mbps")
    print(f"Upload speed: {upload_speed} Mbps")
    if download_speed or upload_speed < 60:
        tweet_at_provider(down=download_speed,up=upload_speed)


def tweet_at_provider(down,up):
    driver.get("https://x.com/login")
    time.sleep(7)

    mail_box = driver.find_element(By.NAME,'text')
    mail_box.send_keys(TWITTER_EMAIL)

    time.sleep(3)

    mail_box.send_keys(Keys.ENTER)
    time.sleep(3)

    mail_box = driver.find_element(By.NAME,'text')
    mail_box.send_keys("nitheeshmk5_")

    time.sleep(3)
    mail_box.send_keys(Keys.ENTER)
    time.sleep(3)
    password = driver.find_element(By.NAME,'password')
    password.send_keys(TWITTER_PASSWORD)
    time.sleep(3)

    password.send_keys(Keys.ENTER)

    time.sleep(13)
    tweet = driver.find_element(By.CSS_SELECTOR, "[data-testid='tweetTextarea_0']")

    tweet.send_keys(f"Hello all,This post was post by python bot !!\nI bought 40mbps plan,Today I got\nUpload speed : {up}\nDownload speed : {down}\n#100daysofpython")
    time.sleep(3)

    tweet.send_keys(Keys.CONTROL,Keys.ENTER)


# call
get_internet_speed()   
#tweet_at_provider(25,90)
    
    
