def solution(dic):
    sum = 0
    for key in dic:
        sum = sum + dic[key]

    return sum

print solution({1:10, 2:20, 3:30})
