from random import randrange

user = 'yes'
while user == 'yes':
    n = randrange(100)
    number_of_guess = 1
    print("you compelete the game in 10 guess")
    while(number_of_guess <= 10):
        guess = int(input("enter the guess no: "))
        if( guess < n ):
            print("your no is small enter the greater no ")
        elif( guess > n ):
            print("your no is greater enter the sammler no ")
        else:
            print("you win")
            print(number_of_guess,"no of guess you complete")
            break
        print(10 - number_of_guess,"no of guess you left")
        number_of_guess = number_of_guess + 1
    if(number_of_guess > 10):
        print("game over")

    user = input("if continue type yes: ")