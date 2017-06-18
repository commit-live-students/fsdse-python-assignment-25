dic1={1:10, 2:20, 3:30}
def solution(dic1):
    sum=0
    value=dic1.values()
    for v in value:
        sum=sum+v
    return sum
solution(dic1)
