
def is_pentagon(num):
    pentagon = str((((num*24 +1)**(1/2)+1)/6))
    if pentagon[-1] == "0":
        return True
    return False

def pentagon(num):
    return num*(3*num-1)/2
    
def solution():   
    for x in range(10,10000):
        for y in range(x,10000):
            num1 = pentagon(x)
            num2 = pentagon(y)    

            if is_pentagon(num1 + num2) == True and is_pentagon(num2 - num1) == True:
                return num2 - num1
            
print(solution())