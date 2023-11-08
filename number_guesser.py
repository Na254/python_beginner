import random

random_number=random.randint(1,100)
attempts=0

print("Welcome to the guess the Number Game")

while True:

    user_game=int(input("Guess the number between 1 and 100 "))
    attempts+=1

    if user_game==random_number:

        print(f"Congratulations!You guessed the number{random_number}correctly in{attempts}attempt.")
        break 
    elif user_game < random_number:

        print("Try a higher number.")

    else:
        print("Try a lower number.")

        





    


