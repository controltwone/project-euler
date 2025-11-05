import random
def isPrime(num):
    if num == 1:
        return False
    for x in range(2, int(num**(1/2))+1):
        if num % x == 0:
            return False
    return True

def concat_anyof_two(mylist : list) -> list:
    sol_list = []
    for x in range(len(mylist)-1):
        for y in range(x+1,len(mylist)):
            num1 = str(mylist[x]) + str(mylist[y])
            num2 = str(mylist[y]) + str(mylist[x])
            sol_list.append(num1)
            sol_list.append(num2)

    return sol_list

       
print(concat_anyof_two([12,8,5,6]))

def findPrimePairSets():
    random_prime = []
    

    
    primeList = []
    for x in range(1,1000):
        if isPrime(x) == True:
            primeList.append(x)

    while True:
        count = 0
        for x in range(5):
            random.choice(primeList)
            random_prime.append(x)

        concats = concat_anyof_two(random_prime)
        for y in concats:
            if isPrime(int(y)) == True:
                count += 1
        if count == 12:
            return concats



print(findPrimePairSets())
