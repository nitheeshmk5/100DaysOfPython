'''
Miles -> Kilometers
1m = 1.6km
'''

from tkinter import * 

screen = Tk()
screen.minsize(width=600,height=300)
screen.title("Miles to Kilometers")

#Miles entry

miles = Entry(width=18)
miles.grid(column=1,row=0)
mi = Label(text="Miles")
mi.grid(column=3,row=0)
mi.config(padx=5,pady=5)

label = Label(text="is equal to ->")
label.grid(column=0,row=1)
label.config(padx=20,pady=20)

def miles_to_km():
    mile = miles.get()
    kilom = round( float(mile) * 1.6 , 2)
    km.config(text=f'{kilom}')
    

km = Label(text='________________________')
km.grid(row=1,column=1)

kilo = Label(text='kilometers')
kilo.grid(row=1,column=2)
kilo.config(padx=10,pady=10)

calc = Button(text="Calculate",command=miles_to_km)
calc.grid(row=2,column=1)

screen.mainloop()