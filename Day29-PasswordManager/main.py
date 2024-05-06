from tkinter import * 
from tkinter import messagebox
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random as rd

def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','0', '1', '2', '3', '4', '5', '6', '7', '8', '9','!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    for i in range(0,12):
        password_list.append(rd.choice(letters))

    rd.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web = web_entry.get()
    pas = password_entry.get()
    email = email_entry.get()
    if len(web) == 0 or len(pas) == 0:
        messagebox.showinfo(title="WARNING",message="Please enter all the feilds..")
    else:
        is_ok = messagebox.askokcancel(title='Confirmation',message=f'Website : {web}\nemail : {email}\npass : {pas}\nPress ok to save ⭕')
        
        if is_ok:
            with open('data.txt','a') as file:
                file.write(f'{web} | {email} | {pas}\n')
                web_entry.delete(0,END)
                password_entry.delete(0,END)
    


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=50,pady=50)
#canvas
img = PhotoImage(file='logo.png')
canvas = Canvas(width=200,height=200)
canvas.create_image(100,100,image=img)
canvas.grid(row=1,column=2)

#website 
website = Label(text='Website : ')
website.grid(row=2,column=1)


web_entry = Entry(width=50)
web_entry.grid(row=2,column=2,columnspan=2)
web_entry.focus()
web = web_entry.get()

#Email 

email_label = Label(text='Email/username : ')
email_label.grid(row=3,column=1)

email_entry = Entry(width=50)
email_entry.grid(row=3,column=2,columnspan=2)
email_entry.insert(0,'nitheeshmk5@outlook.com')


#Password
password = Label(text='Password : ')
password.grid(row=4,column=1)

password_entry = Entry(width=40)
password_entry.grid(row=4,column=2)

password_botton = Button(text='Generate',command=generate_pass)
password_botton.grid(row=4,column=3)

#Add button

add = Button(text='Add',width=35,command=save)
add.grid(row=5,column=2,columnspan=2)

window.mainloop()