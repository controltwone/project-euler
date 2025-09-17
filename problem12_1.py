
def findTriangle(num : int) -> int:
    sum = (num *(num + 1))/2
    return int(sum)

# print(findTriangle(7))

def findFactorsLen(num : int) -> int:
    factors = []
    for i in range(1,num+1):
        if num % i == 0:
            factors.append(i)
    return len(factors)

# print(findFactorsLen(28))

for i in range(20000,30010):
    triangleNum = findTriangle(i)
    numoffactors = findFactorsLen(triangleNum)
    print(i,".triangle number =",triangleNum, "number of factors:",numoffactors)
    # if numoffactors == 501:
    #     print(i)
    #     break 
