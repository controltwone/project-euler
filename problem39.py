def findNumofSol(p : int):
    count = 0
    for x in range(int(p/2) +1):
        for y in range(x, int(p/2) +1):
            z = p - x - y

            if x**2 + y**2 == z**2:
                count +=1

    return count

# print(findNumofSol(120))

def sol():
    max_sol = 0
    for x in range(1,1001):
        num = findNumofSol(x)
        if num > max_sol:
            p = x
            max_sol = num
    return max_sol

print(sol())