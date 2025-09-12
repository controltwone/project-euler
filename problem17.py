dict1 = ["one", "two", "three","four","five","six","seven","eight","nine"]
dict2 = ["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
dict3 = ["twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]

    
def oneandtwo_digits(num : str)-> str:
    
    if(len(num)==1): #1,2..,9 kadar olan rakamları işler.
        digit = int(num[0])
        return dict1[digit-1]
    
    elif 9<int(num)<20:  #10,..,19 arasındaki sayıları işler.
        digit = int(num[1]) 
        return dict2[digit]
    
    elif(int(num[1]) == 0): #10,20,30.. gibi sayıları işler.
        digit = int(num[0])
        return dict3[digit-2]
        
    else:                #kalan 2 basamaklı sayıları işler.
        digit3 = int(num[1])
        digit1 = int(num[0]) 
        return dict3[digit1-2] + dict1[digit3-1]


def threedigits(num :str) -> str:
    if len(num) == 4:
        return "onethousand"
    
    elif int(num[1]) == 0 and int(num[2]) == 0:
        digit = int(num[0])
        return dict1[digit-1]+"hundred"

    elif int(num[0]) == 1:
        if int(num[1])==0:
            digit = int(num[2]) 
            return "onehundredand"+ dict1[digit-1]
        else:
            digit = oneandtwo_digits(num[1:]) 
            return "onehundredand"+ digit
    
    elif int(num[0]) == 2:
        if int(num[1])==0:
            digit = int(num[2]) 
            return "twohundredand"+ dict1[digit-1]
        else:
            digit = oneandtwo_digits(num[1:]) 
            return "twohundredand"+ digit
        
    elif int(num[0]) == 3:
        if int(num[1])==0:
            digit = int(num[2]) 
            return "threehundredand"+ dict1[digit-1]
        else:
            digit = oneandtwo_digits(num[1:]) 
            return "threehundredand"+ digit
        
    elif int(num[0]) == 4:
        if int(num[1])==0:
            digit = int(num[2]) 
            return "fourhundredand"+ dict1[digit-1]
        else:
            digit = oneandtwo_digits(num[1:]) 
            return "fourhundredand"+ digit

    elif int(num[0]) == 5:
        if int(num[1])==0:
            digit = int(num[2]) 
            return "fivehundredand"+ dict1[digit-1]
        else:
            digit = oneandtwo_digits(num[1:]) 
            return "fivehundredand"+ digit

    elif int(num[0]) == 6:
        if int(num[1])==0:
            digit = int(num[2]) 
            return "sixhundredand"+ dict1[digit-1]
        else:
            digit = oneandtwo_digits(num[1:]) 
            return "sixhundredand"+ digit 

    elif int(num[0]) == 7:
        if int(num[1])==0:
            digit = int(num[2]) 
            return "sevenhundredand"+ dict1[digit-1]
        else:
            digit = oneandtwo_digits(num[1:]) 
            return "sevenhundredand"+ digit

    elif int(num[0]) == 8:
        if int(num[1])==0:
            digit = int(num[2]) 
            return "eighthundredand"+ dict1[digit-1]
        else:
            digit = oneandtwo_digits(num[1:]) 
            return "eighthundredand"+ digit

    else:
        if int(num[1])==0:
            digit = int(num[2]) 
            return "ninehundredand"+ dict1[digit-1]
        else:
            digit = oneandtwo_digits(num[1:]) 
            return "ninehundredand"+ digit
    

            
def computeLettersLength() -> int:
    sum = 0

    for num in range(1,1001):
        if len(str(num)) == 3 or len(str(num)) == 4:
            strNum = threedigits(str(num))
            print(strNum)
            lenghtofStr = len(strNum)
            print(lenghtofStr)
            sum +=lenghtofStr
        else:
            strNum = oneandtwo_digits(str(num))
            # print(strNum)
            lenghtofStr = len(strNum)
            # print(lenghtofStr)
            sum +=lenghtofStr
    return sum

print(computeLettersLength())

