def isPrime(num : int):
    if num == 2 :
        return True
    if num == 1 :
        return False

    
    for x in range(2,int(num**1/2) + 1):
        if num % x == 0:
            return False
        
    return True

def truncateNumberLefttoRight(num : str):

    for x in range(len(num)):

        str1 = num[x:]
        # print(str1)

        if isPrime(int(str1)) == False:
            return False
        
    return True

# print(truncateNumberLefttoRight("3797"))

def truncateNumberRighttoLeft(num : str):

    for x in range(len(num)):

        str1 = num[:len(num)-x]
        # print(str1)

        if isPrime(int(str1)) == False:
            return False
        
    return True

# print(truncateNumberRighttoLeft("3797"))

# for x in range(10,1000,2):
    
#     if isPrime(x) == True:
#         str1 = str(x)

def findTruncatablePrimes():
    sum = 0
    count = 0
    for x in range(11,1000000,2):
        if truncateNumberRighttoLeft(str(x)) and truncateNumberLefttoRight(str(x)) == True:
            print(x)
            sum += x
            count += 1
            if count == 11:
                break

    return f"{count} kadar truncatable number ve toplamları {sum}"

print(findTruncatablePrimes())