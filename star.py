
def star(a,b):
    if b == True:
        c = 1
        while c <= a:
            print(c * '*')
            c = c+1
    else:
        while a > 0:
            print(a * '*')
            a = a-1
if __name__ == '__main__':

    x= int(input("enter the number of line you print: "))
    y = bool(int(input("enter 0 to false:  ")))
    print(star(x,y))