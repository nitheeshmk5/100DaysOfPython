from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    title_label.config(text='Timer')
    canvas.itemconfig(timer_text,text='00:00')
    global reps
    reps = 0
    


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    works_sec = WORK_MIN * 60
    break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    #conditions
    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text='Break',fg=RED)
    elif reps % 2 == 0:
        count_down(break_sec)
        title_label.config(text='Break',fg=PINK)
    else:
        count_down(works_sec)
        title_label.config(text='Work',fg=GREEN)
         

    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f'0{count_sec}'

    canvas.itemconfig(timer_text,text=f'{count_min}:{count_sec}')
    if count > 0:
        #print(count)
        global timer
        timer = window.after(1000,count_down,count-1)
    else:
        start_timer()
        marks = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            marks += '✅'
        done.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Pomodoro')
window.config(padx=100,pady=50,bg=YELLOW)

#title label
title_label = Label(text='Timer',font=(FONT_NAME,50,'bold'),bg=YELLOW,fg=GREEN)
title_label.grid(row=1,column=2)
#canvas
img = PhotoImage(file='./asserts/tomato.png')
canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=False)
canvas.create_image(100,112, image=img)

#text
timer_text = canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,'bold'))
canvas.grid(row=2,column=2)

#Start button
start = Button(text='Start',highlightthickness=False,command=start_timer)
start.config(padx=10,pady=5)
start.grid(row=3,column=1)

#Reset button
reset = Button(text='resert',highlightthickness=False,command=reset_timer)
reset.config(padx=10,pady=5)
reset.grid(row=3,column=3)

#Done label
done = Label(text='',highlightthickness=False,fg=GREEN,bg=YELLOW)
done.grid(row=4,column=2)



window.mainloop()