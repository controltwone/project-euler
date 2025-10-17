# import random

# num = [x for x in range(10)]



# def calculateSumFifthPower(liste):
#     sum = 0
#     for num in liste:
#         sum += num**5

#     return sum



# def findNum():
#     sayı = ""
#     while True:

#         sayı += str(random.choice(num))
#         if(len(sayı) == 7):
#             sayı = ""

#         if(sayı == calculateSumFifthPower):
#             return sayı

# print(findNum())
answer = 0

for x in range(100,10000000):
    sum = 0
    num = str(x)

    for y in range(len(num)):
        sum += int(num[y])**5
    
    if num == str(sum) :
        print(num)
        answer += sum   

print(answer)
