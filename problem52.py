def findNum(arr,target):

    for x in arr:
        if x == target:
            return True
    return False

# print(findNum("456","5"))

def haveSameDigit(num1, num2):

    if len(num1) != len(num2):
        return False    
    
    list_num2 = [x for x in num2]
    
    for x in num1:
        if findNum(list_num2, x) == True:
            list_num2.remove(x)
            
        if len(list_num2) == 0:
            return True
        
    return False

print(haveSameDigit("1456","5614"))

def find_smallest_integer():

    for i in range(1,1000000):
        if haveSameDigit(str(i), str(i*2)) == True:

            if haveSameDigit(str(i*2), str(i*3)) == True:

               if haveSameDigit(str(i*3), str(i*4)) == True:
                    
                    if haveSameDigit(str(i*4), str(i*5)) == True:

                         if haveSameDigit(str(i*5), str(i*6)) == True:
                             
                             return i
                         

print(find_smallest_integer())