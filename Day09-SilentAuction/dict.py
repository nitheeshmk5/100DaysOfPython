tourist_spot = [
    {
        'city':'Coimbatore',
        'dailyVisits':100,
        'spots':['Maruthamalai','Isha','Black thunder']
    },
    {
        'city':'Bangalore',
        'dailyVisits':1500,
        'spots':['That temple','This place']
    }
]

def new_details(city,visits,spots):
    new_area = {}
    new_area["city"] = city
    new_area["dailyVisits"] = visits
    new_area["spots"] = spots

    tourist_spot.append(new_area)


new_details("Delhi",2000,['Palace','Red fort'])
print(tourist_spot)

