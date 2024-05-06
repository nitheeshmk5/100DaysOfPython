import datetime as dt 
import pandas,smtplib

my_email = 'nitheesh.muthukrishnanc@gmail.com'
password = 'mysxlatsynxjqzsc'

today = dt.datetime.now()
today_tup = (today.month,today.day)

data = pandas.read_csv('bday.csv')

birthday_dict = {(data_row['month'],data_row['day']) :data_row for(index,data_row) in data.iterrows() }

if today_tup in birthday_dict:
    birthday_person = birthday_dict[today_tup]
    with open('letter.txt') as letter:
        contents = letter.read()
        contents = contents.replace('[name]',birthday_person['name'])
    
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)

        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject:Happy Birthday!!\n\n{contents}"
            )