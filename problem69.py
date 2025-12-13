
# Define a function 'gcd' to calculate the greatest common divisor (GCD) of two positive integers.(EBOB)
def gcd(p, q):
    # Use Euclid's algorithm to find the GCD.
    while q != 0:
        p, q = q, p % q
    return p


# bu fonksiyonun optimizasyonu çok kötü oldu.

# def relatively_prime(num):
#     primes = []
#     factors = findfactors(num)

#     for x in range(1,num):
#         factors_x = findfactors(x)
#         common_factors = False

#         for y in factors_x:
#             if y in factors:
#                 common_factors = True
#                 break
    
#         if not common_factors:
#             primes.append(x)
#     return len(primes)

# def totient_func(num):
#     return len(relatively_prime(num))

def relatively_prime(num):
    primes = []
    for x in range(1, num):
        # Eğer EBOB'ları 1 ise, ortak bölenleri yoktur (aralarında asaldır)
        if gcd(x, num) == 1: 
            primes.append(x)
    return len(primes)


def sol():
    max_value = 0
    max_n = 0
    for n in range(2,1000001):
        value = n  / relatively_prime(n)
        if value > max_value:
            max_value = value
            max_n = n


    return max_value, max_n

print(sol())