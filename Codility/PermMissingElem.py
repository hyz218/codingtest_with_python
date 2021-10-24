def solution(A):
    max_num = len(A)+1
    dp = [i for i in range(1,max_num+1)] #dp list 생성
    num = list(set(dp)-set(A)) #dp 집합에서 A집합에 속한 원소 return
    return num[0] #num이 list 형태로 반환되어 num[0] return