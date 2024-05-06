import smtplib
import datetime as dt
import random

my_email = 'nitheesh.muthukrishnanc@gmail.com'
password = 'mysxlatsynxjqzsc'

now = dt.datetime.now()
week = now.weekday()

if week == 1:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)

        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject:Monday motivation\n\n{quote}"
            )