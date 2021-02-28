#Snake Water Gun Game (Snake beats water, water beats gun , gun beats snake)

import random

chances = 10
no_of_chances= 0
computer_points= 0
human_points= 0
choose = ['s', 'w', 'g']

print(" \t \t \t Snake, Water, Gun!\n \n")
print("\t \t \t s:snake  w:water  g:gun \n")

while no_of_chances < chances:
    ipt= input("Snake, Water or Gun? \n")
    ipt= ipt.lower()
    _random = random.choice(choose)
    
    if ipt == _random:
            print("It's a tie, 0 point to each \n")
    
    elif ipt == "s" and _random == "g":
            computer_points = computer_points + 1
            print(f"You guessed {ipt} and computer guessed {_random} \n")
            print("Computer wins 1 point \n")
            print(f"Computer points: {computer_points} Your points: {human_points}\n")
    
    elif ipt == "g" and _random == "w":
            computer_points = computer_points + 1
            print(f"You guessed {ipt} and computer guessed {_random} \n")
            print("Computer wins 1 point \n")
            print(f"Computer points: {computer_points} Your points: {human_points}\n")

    elif ipt == "w" and _random == "s":
            computer_points = computer_points + 1
            print(f"You guessed {ipt} and computer guessed {_random} \n")
            print("Computer wins 1 point \n")
            print(f"Computer points: {computer_points} Your points: {human_points}\n")

    elif ipt == "w" and _random == "g":
            human_points = human_points + 1
            print(f"You guessed {ipt} and computer guessed {_random} \n")
            print("You win 1 point \n")
            print(f"Computer points: {computer_points} Your points: {human_points}\n")

    elif ipt == "g" and _random == "s":
            human_points = human_points + 1
            print(f"You guessed {ipt} and computer guessed {_random} \n")
            print("You win 1 point \n")
            print(f"Computer points: {computer_points} Your points: {human_points}\n")
    
    elif ipt == "s" and _random == "w":
            human_points = human_points + 1
            print(f"You guessed {ipt} and computer guessed {_random} \n")
            print("You win 1 point \n")
            print(f"Computer points: {computer_points} Your points: {human_points}\n")


    else: 
            print("Wrong input!!")

    no_of_chances = no_of_chances+1
    print(f"{chances-no_of_chances} chances left")
    

print("Game over")

if computer_points> human_points:
        print("You lose , better luck next time")
    
elif human_points > computer_points:
        print("You win!!")

else:
        print("It's a draw")


print(f"You score: {human_points} || Computer score: {computer_points}")

    

    



    