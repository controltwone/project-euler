def fib(num):
    myList = [1,1,2]

    if num == 1 or num == 2:
        return 1
    
    else:
        for x in range(1,num):
            myList.append(myList[x + 1] + myList[x])

        return myList[num-1]



        
# print(len(str(fib(4782))))
    

def finddigit():
    i = 1
    while True:
        if len(str(fib(i))) == 1000:
            return i
        i += 1

print(finddigit())