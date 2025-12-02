def isPrime(num: int):
    for x in range(3,int(num**(1/2)+1)):
        if num % x == 0:
            return False   
        
    return True

# print(isPrime(1487))

def isPermutations(num1, num2):
    return sorted(str(num1)) == sorted(str(num2))
# print(isPermutations(1487,8142))

def solution():
    mylist = []
    for x in range(1000,10000):
        if isPrime(x) != True:
            continue
        term2 = x + 3330
        term3 = term2 + 3330
        if isPrime(term2) == True and isPrime(term3) == True:
            if isPermutations(x,term2) == True and isPermutations(term2, term3) == True:
                mylist.append(str(x)+str(term2)+str(term3))
    return mylist
print(solution())