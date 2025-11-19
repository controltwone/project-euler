from fractions import Fraction

print(Fraction(0.25))


def recursion(num):
    if num == 0:
        return 0

    return 1/(2 + recursion(num-1))

print(recursion(1000))