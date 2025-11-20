def squareofalldigits(num: int) -> int :

    num1 = str(num)
    mylist = [int(digit) for digit in num1]
    square = sum([digit*digit for digit in mylist])
    

    if square == 89:
        return True
    
    if square == 1:
        return False


    return squareofalldigits(square)

print(squareofalldigits(37))


def findSolution():
    count = 0
    for x in range(1,10000000):
        if squareofalldigits(x) == True:
            count += 1
    return count


print(findSolution())