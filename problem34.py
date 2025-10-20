def findFactorial(num : int):
    product = 1
    for x in range(1, num+1):
        product *= x
    
    return product

# print(findFactorial(9))

def findSumofFactorial(num : str):
    sum = 0
    for y in num:
        sum += findFactorial(int(y))
    return sum

# print(findSumofFactorial("145"))

for x in range(10,100000000):
    if x == findSumofFactorial(str(x)):
        print(x)