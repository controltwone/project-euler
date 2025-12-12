def isPrime(num):
    if num == 1:
        return False
    if num == 2 or num == 3:
        return True
    for x in range(2, int(num**(1/2))+1):
        if num % x == 0:
            return False
    
    return True

print(isPrime(13))

def sol():
    prime_list = [x for x in range(2,10000) if isPrime(x) == True]
    max_count = 0

    most_sum = 0
    for i in range(len(prime_list)):
        sum = prime_list[i]
        count = 0

        
        for x in range(i+1, len(prime_list)):
            count += 1
            sum += prime_list[x]

            if sum > 1000000:
                break
            
            

            if isPrime(sum) :
                # print(sum)
                if count > max_count:
                    max_count = count
                    most_sum = sum
          
        
    return most_sum, max_count

print(sol())