def isPrime(num):
    if num <= 1:
        return False
    
    if num == 2:
        return True
    
    if num % 2 == 0:
        return False

    for x in range(3, int(num**(1/2)) + 1, 2):
        if num % x == 0:
            return False
            
    return True

print(isPrime(41))


def quadratic_func(a,b,x):
    return x*x + a*x + b

def sol():
    max_count = 0
    product_coefficient = 1
    
    for a in range(-999,1000):
        for b in range (-1000, 1001):
            x = 0
            while isPrime(quadratic_func(a,b,x)):
                x += 1
                
            if x > max_count:
                max_count = x
                product_coefficient = a*b
                
                
            
    return product_coefficient

print(sol())