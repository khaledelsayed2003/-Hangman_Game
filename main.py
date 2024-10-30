import random
import words_list

name=input("What is your name player?\n")
print(f"Welcome to guessing the right word game! {name}")

ques1=input("Are you ready? Answer by typing yes or no\n")

if ques1.lower() == "yes" or ques1.lower() == "yep" or ques1.lower() == "yeah" or ques1.lower() == "yup":
    print("Before you start you should know that each wrong guess will make you lose a life . You have 6 lives.\n")
    answer=(input("Are you still willing to play? Type yes or no\n"))
    if answer.lower() == "yes" or answer.lower() == "yep" or answer.lower() == "yeah" or answer.lower() == "yup":

        word_list=words_list.word_list
        chosen_word= random.choice(word_list)
        # print(chosen_word)                    
   
        placeholder=""
        for letter  in chosen_word:
            placeholder += "_"

        print(placeholder)                    


        correct_letter=[]
        game_over=False
        list_of_life=["game over","opps! be careful.. 1 life left","lost four lives","opps! lost three lives", "opps! lost two lives", "lost one life","no loosing lives "]
        num_of_life=6


        while not game_over:
    

            guess=input("Guess a letter?\n").lower()  
            display=""
    
            for letter in chosen_word:
    
                if letter == guess:
                    display += guess
                    if guess in correct_letter:
                        print(f"You guessed {guess} before")
                    correct_letter.append(guess)
            
                elif letter in correct_letter:
                    display += letter
            
                else:
                    display += "_"
            print(display)
    
    
            if guess not in chosen_word:
                num_of_life-=1
                if num_of_life==0:
                    game_over=True
                    print("You lose")
    
    
    
            if "_" not in display:
                game_over=True
                print("You win, Congrats man/woman! you are smart as fuck.")
        
        
            print(list_of_life[num_of_life])
    
    else:
        print("We are sad to see you go, but we hope you can play this game one-day")

    
else:
    print("Please get ready to play guessing the right word game, Then get back!")











# for  letter in chosen_word:     

    
#     if guess==letter:
#         print("Right")
#     else:
#         print("Wrong")
#     # \end{code}
    