user = 'yes'
while(user == 'yes'):
    def fact(n):
        if n == 1:
            return 1
        else:
            return n * fact(n-1)

    if __name__ == '__main__':
        x = int(input("enter the number: "))
        print(fact(x))
    user = input("enter yes to continue: ")
