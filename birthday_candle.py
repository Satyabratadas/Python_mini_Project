def birthday(arr):
     count = 0
     big = max(arr)
     for i in range (len(arr)):
         if(arr[i] == big):
             count += 1
     return count

if __name__ == '__main__':
    arr = []
    n = int(input("enter the size of list"))

    for i in range(0,n):
        x = int(input())
        arr.append(x)
    #print(list)
    p = birthday(arr)
    print('Max candles are:- ',p)



