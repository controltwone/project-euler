
maximum = 1
for x in range(100,1000):
    for y in range(100,1000):
        num = str(x*y)

        if(num[0] == num[-1]):
            if(num[1] == num[-2]):
                if(num[2] == num[-3]):
                    if(int(num) > maximum):
                        maximum = int(num)
        
print(maximum)

