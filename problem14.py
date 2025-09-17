def collatz_length(num):
    count = 0
    while num > 1:
    
        if num % 2 == 0:
            num /= 2
            count+=1
        else:
            num = num*3 + 1   
            count += 1

    return count +1

# print(collatz_length(13))

def find_chain():
    max = 0
    iterator = 0
    for i in range(1000000):
        len = collatz_length(i)
        if len > max:
            max = len
            iterator = i
    return max, iterator

print(find_chain())