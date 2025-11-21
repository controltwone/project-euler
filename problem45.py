def func():

    for y in range(1000,100000):

            for x in range(y,100000):

                if x*(3*x-1)/2 == y*(2*y-1):
                    
                    return x, y
                
# print(func())

# print(27693*(2*27693-1))

def func1():
    for x in range(1000,100000):
        if x*(x+1)/2 == 1533776805:
            return x
        
print(func1())