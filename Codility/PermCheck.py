def solution(A):

    A.sort() #A 정렬하기
    for i in range(len(A)): #A의 길이만큼 도는 반복문
        if (i+1) != A[i]: #i+1이 A[i]의 원소값과 다르면 0 반환
            return 0
    
    return 1 #조건에 충족할 경우 1 반환