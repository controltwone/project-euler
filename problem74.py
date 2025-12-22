def factorial(num):
    if num <= 1:
        return 1
    
    return num * factorial(num-1)

# print(factorial(5))

def sumFactoriels(num):
    num_str = str(num)
    sum = 0
    for digit in num_str:
        sum += factorial(int(digit))
    return sum

# print(sumFactoriels(169))

def findChainLen(num):
    chain = [num]
    curr = num
    

    while True:
        curr = sumFactoriels(curr)

        if curr in chain:
            return len(chain)

        chain.append(curr)
# print(findChainLen(540))
    
def sol():
    count = 0
    for x in range(1,1000001):
        if findChainLen(x) == 60:
            count += 1
    return count

print(sol())