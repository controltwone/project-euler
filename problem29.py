a = [ x for x in range(2,101)]
b = [ x for x in range(2,101)]


numbers = []

for base in a:
    for exp in b:
        numbers.append(base**exp)

print(len(numbers))

numberSet = list(set(numbers))
print(len(numberSet))