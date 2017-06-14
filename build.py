def solution(dic):
    sum = 0
    for x,y in dic.items():
        sum = sum + y
    return sum
print (solution({1: 10, 2: 20, 3: 30, 4: 40}))
