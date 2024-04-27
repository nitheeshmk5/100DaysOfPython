from data import python_quiz

class Quiz():
    def __init__(self):
        pass
    
    def display_ques(self):
        game_on = True
        score = 0
        i = 0
        while game_on:
            dictionary = python_quiz[i]
            ques = dictionary['text']
            ans = dictionary['answer'].lower()
            print(f"Question : {ques} ?")
            user_answer = input("Enter (true / false) :")

            if user_answer == ans:
                score += 1
                i+=1
                print(f"Score : {score}")
                game_on = True
            else:
                print("Good try !! ")
                print(f"final score is : {score}")
                game_on = False
        
        

quiz = Quiz()
quiz.display_ques()

        
        





    

