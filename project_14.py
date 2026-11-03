
import random

print("WELCOME TO GAME SIMULATOR")


print("choose the number")

print("(1) coin simulator\n" "(2)rock paper scissor \n" "(3) gussing game \n" )

user_input = int(input("enter the number :"))
points = 0

if user_input == 1:
    
    

    print("welcome to coin simulator")

    import random
    Choice = ("head","tail")
    user_choice = input("enter head or tail :").lower()
    computer_choice = random.choice(Choice)
    print (f"the computer choice is : {computer_choice}")

    if user_choice == computer_choice:
        print("YOU WON")

    elif user_choice != computer_choice :
        print("YOU LOOSE")
    else:
        print("invalid input")

elif user_input == 2:
    print("welcome to rock , paper, scissor")

    import random
    CHOICE = ("rock","paper","scissor")
    user_choice = input("enter rock ,paper or scissor :")
    computer_choice = random.choice(CHOICE)
    print(f"computer choice is : {computer_choice}")

    if user_choice == computer_choice:
        print("THE GAME IS DRAW")

    elif user_choice == "rock" and computer_choice == "scissor" or\
            user_choice == "paper" and computer_choice =="rock" or\
             user_choice =="scissor" and computer_choice == "paper" :
        print("YOU WON THE GAME")

    else:
        print("YOU LOOSE")

elif user_input == 3:
    print("WELCOME TO GUSSING GAME")
    turns = 0
    n = 3
    points = 0

    import random
    computer_choice = random.randint(1,100)
    
    while turns < n:

        user_choice = int(input("ENTER number from 1 to 100 :"))
        

        if user_choice ==computer_choice:
            points += 20
            print("YOU GUSSED THE NUMBER")

        elif user_choice > computer_choice:
            print("tooo high")

        elif user_choice < computer_choice:
            print("tooo low")
        else:
            print("invalid input")

        print(f"total points : {points}")
        

        turns += 1

    
    print(f"total points {points}")

else:
    print("invalid input")

    





