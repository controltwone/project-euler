
def sol():
    count = 0
    for base in range(1,350):
        for power in range(1,350):
            num = base**power
            if len(str(num)) == power:
                count += 1
                print(num)
    return count

print(sol())