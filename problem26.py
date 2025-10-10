
def findPattern(num):
    
    diff = 0
    for i in range(len(num)):
        for x in range(i+1,len(num)):
            if num[i] == num[x]:
                diff = x - i
                return diff
    return 0
maximum = 0
c = 0
for num in range(11,1000):
    a = (str(1/num))[2:]
    b = findPattern(a)  
    maximum = b


    if maximum > c:
        c = maximum
        d = num


# print(type(str(1/998)))
print(c , d)