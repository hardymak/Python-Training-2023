import random

game = """
            GAME - ROCK PAPER SCISSOR

            SELECT YOUR CHOICE

            ROCK
            PAPER
            SCISSOR

"""
print(game)

Game_list = ["ROCK","PAPER","SCISSOR"]

C_Choice = random.choice(Game_list)

status = True
C_Score = 0
U_Score = 0

while status:
    
    U_Choce = input("Enter Your Choice : ").upper()
    C_Choice = random.choice(Game_list)
    
    print("COMPUTER SELECTED : ",C_Choice )
    print("USER SELECTED : ", U_Choce)
    
    if U_Choce == C_Choice:
        print(" TIE ")
    elif U_Choce == "ROCK" and C_Choice == "PAPER" :
        print(" COMPUTER WON !!! ")
        C_Score += 1
    elif U_Choce == "ROCK" and C_Choice ==  "SCISSOR" :
        print(" USER WON !!! ")
        U_Score += 1
    elif U_Choce == "SCISSOR" and C_Choice == "PAPER" :
        print(" USER WON !!! ")
        U_Score += 1
    elif U_Choce == "SCISSOR" and C_Choice ==  "ROCK" :
        print(" COMPUTER WON !!! ")
        C_Score += 1
    elif U_Choce == "PAPER" and C_Choice == "ROCK" :
        print(" USER WON !!! ")
        U_Score += 1
    elif U_Choce == "PAPER" and C_Choice ==  "SCISSOR" :
        print(" COMPUTER WON !!! ")
        C_Score += 1

    choice = input ("Do You Want to Continue Y FOR Yes N for No : " )

    if choice == "n" :
        status = False

print(f" USER SCORE : {U_Score}")
print(f" USER SCORE : {C_Score}")