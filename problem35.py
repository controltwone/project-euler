def isPrime(num : int):
    if num == 1 or num == 2:
        return True
    
    for x in range(2, int(num**1/2) + 1):
        if num % x == 0:
            return False
        
    return True

# print(isPrime(971))

def isCircularPrime(num : str):


    for x in range(len(num)):
        str1 = num[0]
        str2 = num[1:] 
        str3 = str2 + str1

        if str3 == num:
            break

        if isPrime(int(str3)) == False:
            return False    
        
        num = str3
        # print(str3)

      
    
    return True

# print(isCircularPrime("1193"))

def findCircularPrimesUnderMillion():
    sum = 0
    for x in range(100,1000001):
        if isCircularPrime(str(x)) == True:
            sum += 1 
    
    return sum

print(findCircularPrimesUnderMillion())

# 78