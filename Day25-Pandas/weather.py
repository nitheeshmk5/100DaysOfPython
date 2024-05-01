# with open('weather_data.csv') as data:
#     datas = data.readlines()
#     print(datas)

import csv
import pandas

with open('weather_data.csv') as data:
    datas = csv.reader(data)
    temp = []
    for i in datas:
        if i[1] != "temp":
            temp.append(int(i[1]))
            
    print(temp)


#Using pandas
datas = pandas.read_csv('weather_data.csv')
print(datas)

#Average of the temperature

temps = datas['temp'].to_list()
avg = sum(temps)/len(temps)
print(avg)
#mean
mean = datas['temp'].mean()
print(mean)
