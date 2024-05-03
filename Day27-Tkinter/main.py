from tkinter import * 

window = Tk()
window.minsize(width=500,height=400)
window.title("New tkinter GUI")

label = Label(text="Nitheesh's GUI",font=('Arial',22,'normal'))
label.pack()

#Entry

inp = Entry(width=15)
inp.pack()

def button_clicked():
    value = inp.get()
    label.config(text=f"entered : {value}")

button = Button(text="Click me",command=button_clicked)
button.pack()

window.mainloop()