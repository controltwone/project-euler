# print(ord("B")-64)


with open("0022_names.txt","r") as file:
    words = file.read()

words_1 = [x.strip('"') for x in words.split(",")] 
words_1.sort()




# print(words_1[937]) it must returns the COLIN

def solution():
    count_order = 0
    total_score = 0
    for x in words_1:
        count_order += 1
        sum = 0
        score = 0
        l = len(x)
        for y in range(l):
            sum += ord(x[y])-64

        score = count_order*sum
        total_score += score

    return total_score

print(solution())


