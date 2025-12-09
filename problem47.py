def isPrime(num):
    if num == 2 and num == 3:
        return True
    for x in range(2, int(num**(1/2))+1):
        if num % x == 0:
            return False
    
    return True

def findFactors(num):
    return [x for x in range(2,num) if num % x == 0 and isPrime(x) == True ]

print(findFactors(646))

def solution():
    for y in range(10000, 10000000):
        count = 0
        for z in range(y, y+4):
            if len(findFactors(z)) == 4:
                count += 1
            else:
                break
            if count == 4:
                return z - 3

print(solution())
                
            