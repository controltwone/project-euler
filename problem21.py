def findSumofDivisors(num: int) -> list:
    
    return sum([x for x in range(1,int(num/2+1)) if num%x == 0])

print(findSumofDivisors(220))

def solution():
    amicable_list = []
    x = 1
    while x<10000:
        a = findSumofDivisors(x)
        if findSumofDivisors(a) == x and a != x:
            if x and a not in amicable_list:
                amicable_list.append(x)
                amicable_list.append(a)
        x += 1
    return sum(amicable_list)

print(solution())