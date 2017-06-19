def solution(dic):
    sum = 0
    for key in dic:
        sum += dic[key]
    return sum


dic = {1:90, 2:100, 3:1200}
solution(dic)
