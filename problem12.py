def findTriangle(num : int) -> int:
    sum = (num *(num + 1))/2
    return int(sum)

# print(findSum(5))

def findFactorsLen(num : int) -> int:
    factors = []
    for i in range(1,num+1):
        if num % i == 0:
            factors.append(i)
        
    return len(factors)

# print(findFactors(12340))

for i in range(200000,200010,5):
    print(findFactorsLen(findTriangle(i)))
    # if findFactors(findSum(i)) == 501:
    #     print(i) 

