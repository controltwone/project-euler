def combination(n,r):

    return factoriel(n) // (factoriel(r) * factoriel(n - r))

def factoriel(x):
    product = 1
    for i in range(1,x+1):
        product *= i

    return product

print(factoriel(5))
print(combination(5,2))