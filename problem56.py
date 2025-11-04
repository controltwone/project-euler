
def calculate_sum_of_digit(num : int):
    list_num = [int(x) for x in str(num)]
    sum = 0
    for i in list_num:
        sum += i    

    return sum

# print(calculate_sum_of_digit(23123))


def max_digit_sum():
    max = 1
    for x in range(1,100):
        for y in range(1,100):
            value = calculate_sum_of_digit(x**y)
            if value > max:
                max = value
    return max 




print(max_digit_sum())