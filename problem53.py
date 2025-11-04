def combination(n,r):

    return factoriel(n) // (factoriel(r) * factoriel(n - r))

def factoriel(x):
    product = 1
    for i in range(1,x+1):
        product *= i

    return product

# print(factoriel(5))
# print(combination(5,2))

count = 0

for x in range(1,101):
    for y in range(1,x+1):
        if combination(x,y) > 1000000 :
            count += 1

print(count)