from fractions import Fraction

import sys
sys.setrecursionlimit(2000)  # Limiti 2000'e çıkar


def square_root(num):
    if num == 0:
        return 0

    return Fraction(1, 2 + square_root(num - 1))


def sol():
    count = 0
    for x in range(1,1001):
        value = 1 + square_root(x)
        if len(str(value.numerator)) > len(str(value.denominator)):   
            count += 1
    return count

print(sol())