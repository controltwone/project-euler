def solution() -> int:
    sum = 0
    for x in range(1,1001):
        sum += x**x
    str_sum = str(sum)
    last_ten_digits = str_sum[-10:]
    return last_ten_digits
print(solution())