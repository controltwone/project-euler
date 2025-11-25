# odd composite number : prime olmayan tek sayılar.  

def isPrime(num :int) -> bool:
    if num == 2 or num == 3:
        return True
    
    for x in range(2,int(num**(1/2))+1):
        if num % x == 0:
            return False
    return True

def isOddComposite(num : int) -> bool:
    if num % 2 == 1:
        if isPrime(num) == False:
            return True
    return False 

odd_composite_numbers = [num for num in range(9,10000) if isPrime(num) == False and num%2 == 1]

# print(odd_composite_numbers)

def rule(num:int) -> bool:
    x = 1
    while True:
        prime_ = num - 2*(x**2)
        if prime_ < 2:
            break

        if isPrime(prime_) == True:
            return True
        
        x = x+1
    return False

print(rule(27))

def solution():
    for num in odd_composite_numbers:
        if rule(num) == False:
            return num
        
print(solution())

