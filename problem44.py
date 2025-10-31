
def pentagonal(n : int) ->  int :
    num = n*(3*n - 1)/2
    return num

pent = []
for i in range(1,10000):
    pent.append(pentagonal(i))


for  x in range(len(pent)):
    for y in range(len(pent)):
        if x + y in pent and abs(x-y) in pent:
            sol = abs(x - y)
            minimum = min(sol,10000)
print(minimum)