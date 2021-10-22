def solution(A):
    A.sort() #A를 오름차순으로 정렬 
    cnt=1 #cnt 초기화
    for i in range(len(A)-1):
        if A[i]!=A[i+1]: #A[i]와 A[i+1]이 다른 경우
            if cnt%2==1: #짝이 안맞는 경우 그 숫자 return
                return A[i]
            cnt=1
        else: #A[i]와 A[i+1]가 같은 경우 숫자 더하기
            cnt+=1

    return A[-1]