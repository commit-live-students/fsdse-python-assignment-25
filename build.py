def solution(dic):
    sum = 0
    for e in dic:
        sum = sum+dic[e]
    print sum
    return sum

solution({1:10,2:20,3:30})
