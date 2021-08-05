import random
list1 = ["s","p","b"]

chance = 10
no_of_chance = 0
user_point = 0
computer_point = 0

print("\t \t \t Stone,Paper,Bulet Game\n")
print(" s for Stone \n p for Paper \n b for Bulet \n")

while (no_of_chance<chance):
    user_input = input("enter s or p or b: ")
    computer_input = random.choice(list1)

    if(user_input == computer_input):
        print("Its tie both are 0 point \n")

    elif(user_input == "s" and computer_input == "b"):
        user_point = user_point + 1
        print(f"Your guess {user_input} and Computer guess is {computer_input}\n")
        print("You get 1 point\n")
        print(f"Your point {user_point} Computer point {computer_point}\n")
    elif(user_input == "b" and computer_input == "p"):
        user_point = user_point + 1
        print(f"Your guess {user_input} and Computer guess is {computer_input}\n")
        print("You get 1 point\n")
        print(f"Your point {user_point} Computer point {computer_point}\n")
    elif(user_input == "p" and computer_input == "s"):
        user_point = user_point + 1
        print(f"Your guess {user_input} and Computer guess is {computer_input}\n")
        print("You get 1 point\n")
        print(f"Your point {user_point} Computer point {computer_point}\n")
    elif(user_input == "s" and computer_input == "p"):
        computer_point = computer_point + 1
        print(f"Your guess {user_input} and Computer guess is {computer_input}\n")
        print("Computer get 1 point\n")
        print(f"Your point {user_point} Computer point {computer_point}\n")
    elif(user_input == "p" and computer_input == "b"):
        computer_point = computer_point + 1
        print(f"Your guess {user_input} and Computer guess is {computer_input}\n")
        print("Computer get 1 point\n")
        print(f"Your point {user_point} Computer point {computer_point}\n")
    elif(user_input == "b" and computer_input == "s"):
        computer_point = computer_point + 1
        print(f"Your guess {user_input} and Computer guess is {computer_input}\n")
        print("Computer get 1 point\n")
        print(f"Your point {user_point} Computer point {computer_point}\n")
    else:
        print("Enter the valid input")    

    no_of_chance = no_of_chance + 1
    print(f"You left {chance - no_of_chance} chance out of {chance} \n")
print("Game Over !!")

if(user_point == computer_point):
    print("Tie")
elif(user_point > computer_point):
    print("You Win !!")
else:
    print("Computer Win !!")


