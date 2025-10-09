
import math


def findSumofDivisors(num):
    root = math.ceil(math.sqrt(num))
    total = 1
    divisor = 2
    while(divisor < root):
        if num % divisor == 0:
            total += divisor
            total += num // divisor

        divisor += 1

    if num == root**2:
        total += root

    return total


abundant_numbers = [i for i in range(12,28124) if i < findSumofDivisors(i)]
 
numbers = [False]*28124

for x in range(len(abundant_numbers)):
    for y in range(len(abundant_numbers)):
            s = abundant_numbers[x] + abundant_numbers[y]

            if s < 28123:
                 numbers[s] = True

result = sum([i for i in range(1,28124) if numbers[i]== False])
print(result)

    