def solution(dic):
    x=0
    for k,v in dic.items():
        x+=v
    return x

d={1:10, 2:20, 3:30}
print(solution(d))
