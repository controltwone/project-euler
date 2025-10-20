num = 58533231123123

binary_num = bin(num) 

print(binary_num[2:])

def isPalindome(num : str):
    str1 = num[::-1]

    if str1 == num:
        return True
    
    return False

print(isPalindome("1113111"))

def findBothBases():
    sum = 0
    for x in range(1000001):
        if isPalindome(str(x)) == True:
            binary_num = bin(x)[2:]
            if isPalindome(str(binary_num)) == True:
                sum += x
            
    return sum 
print(findBothBases())