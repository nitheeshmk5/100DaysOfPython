import requests
from bs4 import BeautifulSoup
import lxml
import smtplib,os,dotenv

dotenv.load_dotenv()

USER = os.getenv('my_email')
PASSWORD = os.getenv('password')

product_url = 'https://www.amazon.in/Dell-KB216-Wired-Multimedia-Keyboard/dp/B00ZYLMQH0/ref=sr_1_1_sspa?crid=1WQUL80EQRMDB&dib=eyJ2IjoiMSJ9.Ij8R3a5E-4kDClXwBILtuk-ZeEfjEBsBoUer9z-J5mPMD5m9fBpnJ32frKdQLQ09nwcSMCFoC7vWPhIvIxc_8aElVs9yU_2xmuvVpfl2R0L2osWgCmPxuR8TgHSGhRUUPUIbm2R82uXnY5KTTrcl-dX5zcSwX0OO1OotqL-KgjtnsxR1_KcUW3oXMm0l9fANz1HU7uc7ou5HaByxHnIimmBPD9Y5wSTH7LC9Ox0KdVI.gdPHQCwEbfE1BsbCG0tWcVyZNaSMyW-1h28QOcQP2V8&dib_tag=se&keywords=keyboard&qid=1715915048&sprefix=keyboard+%2Caps%2C241&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1'

head ={
    'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'Accept-Language':'en-US,en;q=0.5'
}
res = requests.get(url=product_url,headers=head)
contents = res.text

soup = BeautifulSoup(contents,'lxml')
price = soup.find(name='span',class_='a-price-whole').getText().split('.')[0]

if price < 450:
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(
            user= USER,
            password=PASSWORD
        )

        connection.sendmail(
            from_addr=USER,
            to_addrs='22107041@srcas.ac.in',
            msg=f'Subject:Keyboard is under price!\nDell keyboard is now {price}'
        )