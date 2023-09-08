""" conditions for win the game (Rock, Scissor and Paper) -
if Rock vs paper -> paper win
if rock vs scissor -> rock win 
if paper vs scissor -> scissor win
"""

import random 
random_list=["rock","paper","scissor"]

while True:
    your_count=0
    computer_count=0 

    uc=int(input("""
                Game start:- 
                 1. Yes
                 2. No | Exit               
                
                  """))
    
    if uc==1:
        for a in range(1,6):
            user_input=int(input("""
                                1.rock
                                 2.scissor
                                 3.paper                          

                                 """))
            
            if user_input==1:
                your_choice="rock"
            if user_input==2:
                your_choice="scissor"
            if user_input==3:
                your_choice="paper"

            computer_choice=random.choice(random_list)

            
            if(your_choice==computer_choice):
                print("your_choice: ", your_choice)
                print("computer_choice: ", computer_choice)
                print("Draw Game")
                your_count=your_count+1
                computer_count=computer_count+1

            elif (your_choice=="rock" and computer_choice=="scissor") or (your_choice=="scissor" and computer_choice=="paper") or (your_choice=="paper" and computer_choice=="rock"):
                print("your_choice: ", your_choice)
                print("computer_choice: ", computer_choice)
                print("You win")
                your_count=your_count+1
                
            else:
                print("your_choice: ", your_choice)
                print("computer_choice: ", computer_choice)
                print("Computer win")
                computer_count=computer_count+1


        if(your_count==computer_count):
            print("Final Game Draw....")
            print("your total score: ", your_count)
            print("Computer total score: ", computer_count)

        elif(your_count>computer_count):
            print("You Win The Game")
            print("your total score: ", your_count)
            print("Computer total score: ", computer_count)

        elif(your_count<computer_count):
            print("Computer Win The Game ")
            print("your total score: ", your_count)
            print("Computer total score: ", computer_count)
        
    else: 
        break
