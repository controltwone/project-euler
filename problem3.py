from math import sqrt

def printFactor(x):
    factors = []
    for x in range(1, int(sqrt(x))+1):
        factors.append(x)

    return factors

print(printFactor(169))

def primeFactors(x):
    for i in x:
        for a in range(x):
            dd