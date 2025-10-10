k = 1001
size = 3  
# size 3,5,7,9,11 ... diye artar 
sum = 1
i = 1 #şuanda 1.sayıdayız.

while size < k+1:
    for n in range(4):  # for 4 edge numbers in each square
        i += size - 1  # şuanda merkezdeki 1in değeri
        sum += i
    size += 2

print(sum)