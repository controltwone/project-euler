def findSum(num : int) -> int:
    sum = (num*(num+1))/2
    return int(sum)

print(findSum(15))

def findFactors(num : int) -> list:
    factors = []
    for i in range(1,num+1):
        if num % i == 0:
            factors.append(i)
    return factors

print(findFactors(140000))