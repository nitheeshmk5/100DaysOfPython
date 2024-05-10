from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface():
    def __init__(self,quiz_brain:QuizBrain) -> None:

        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzeler")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)

        self.score_label = Label(text='Score : 0',fg='white',bg=THEME_COLOR)
        self.score_label.grid(row=0,column=1)

        #Canvas
        self.canvas = Canvas(width=300,height=250,bg='white')
        self.ques = self.canvas.create_text(150,125,width=280,text='Some question')
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)

        true_img = PhotoImage(file='images/true.png')
        self.true_button = Button(image=true_img,command=self.true_pressed)
        self.true_button.grid(row=2,column=0)

        false_img = PhotoImage(file='images/false.png')
        self.false_button = Button(image=false_img,command=self.false_pressed)
        self.false_button.grid(row=2,column=1)

        self.get_next_question()

        self.window.mainloop()
    
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"score : {self.quiz.score}")
            ques_text = self.quiz.next_question()
            self.canvas.itemconfig(self.ques, text=f'{ques_text}')
        else:
            self.canvas.itemconfig(self.ques,text="The End")
    
    def true_pressed(self):
        is_right = self.quiz.check_answer('True')
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer('False')
        self.give_feedback(is_right)
    
    def give_feedback(self,right):
        if right:
            self.canvas.config(bg="green")
        else : self.canvas.config(bg='red')

        self.window.after(1000,self.get_next_question)

        
        
