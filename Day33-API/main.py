import requests,datetime,smtplib


#India
MY_LATITUDE = 20.593683 
MY_LONGITUDE = 78.962883

my_email = 'nitheesh.muthukrishnanc@gmail.com'
password = ''

def iss():
    response = requests.get(url='http://api.open-notify.org/iss-now.json')

    data = response.json()
    latitude = float(data['iss_position']['latitude'])
    longitude = float(data['iss_position']['longitude'])


    if MY_LATITUDE-5 <= latitude <= MY_LATITUDE+5 and MY_LONGITUDE-5 <= longitude <= MY_LONGITUDE+5:
        return True

def is_night():
    parameters = {
        'lat':MY_LATITUDE,
        'lng':MY_LONGITUDE,
        'formatted':0
    }

    current_time = datetime.datetime.now()
    response = requests.get(url='https://api.sunrise-sunset.org/json',params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data['results']['sunrise'].split("T")[1].split(':')[0])
    sunset = int(data['results']['sunset'].split("T")[1].split(':')[0])

    if current_time.hour <= sunrise or current_time.hour >= sunset:
        return True


if iss() and is_night():
    # send mail
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)

        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject:ISS Overhead\n\nThe iss is over you. Look up"
        )


