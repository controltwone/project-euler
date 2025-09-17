from itertools import cycle
import itertools
from math import sqrt

def prime_generator():
    primes = []
    for candidate in itertools.count(2):
        for prime in primes:
            if candidate % prime == 0:
                break
        else:
            yield candidate
            primes.append(candidate)

gen = prime_generator()
for _ in range(10):
    print(next(gen))