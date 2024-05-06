from tkinter import *
import random
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"

datas ={}

try:
    to_learn = pd.read_csv('./data/words_to_learn.csv')
except FileNotFoundError:
    original_data = pd.read_csv('./data/tamil_words.csv')
    datas = original_data.to_dict(orient='records')
else:
    datas = to_learn.to_dict(orient='records')

current_card = {}

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    if datas:
        current_card = random.choice(datas)
        canvas.itemconfig(lang, text="Tamil", fill='black')
        canvas.itemconfig(word, text=current_card['Tamil'], fill='black')
        canvas.itemconfig(card_bg, image=ques_bg)
        flip_timer = window.after(3000, func=flip_card)

def flip_card():
    if current_card:
        canvas.itemconfig(lang, text='English', fill='white')
        canvas.itemconfig(word, text=current_card['English'], fill='white')
        canvas.itemconfig(card_bg, image=ans_bg)

def handle_right():
    if current_card in datas:
        datas.remove(current_card)
        data = pd.DataFrame(datas)
        data.to_csv('./data/words_to_learn.csv', index=False)
    next_card()

def handle_wrong():
    next_card()

# Create the main window
window = Tk()
window.title('Learn Tamil Flashcards')
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

# Create canvas for displaying flashcards
canvas = Canvas(width=800, height=526, highlightthickness=0)
ques_bg = PhotoImage(file='./images/card_front.png')
ans_bg = PhotoImage(file='./images/card_back.png')
card_bg = canvas.create_image(400, 263, image=ques_bg)
lang = canvas.create_text(400, 150, text='', font=('Arial', 40, 'italic'))
word = canvas.create_text(400, 263, text='', font=('Arial', 60, 'bold'))
canvas.config(bg=BACKGROUND_COLOR)
canvas.grid(row=0, column=0, columnspan=2)

# Create 'Right' button for correct response
right_img = PhotoImage(file='./images/right.png')
right = Button(image=right_img, highlightthickness=0, command=handle_right)
right.grid(row=2, column=1)

# Create 'Wrong' button for incorrect response
unknown_img = PhotoImage(file='./images/wrong.png')
unknown = Button(image=unknown_img, highlightthickness=0, command=handle_wrong)
unknown.grid(row=2, column=0)


flip_timer = window.after(3000, flip_card)
next_card()


window.mainloop()
