def solution(N): #O(N) & N=1 error
    min_value = 1e9  #min_value에 무한값 대입
    for i in range(1,N//2+1): #1부터 N//2+1까지 도는 반복문
        if N%i==0: #i가 N의 약수이면
            min_value = min(min_value, (N//i+i)*2) #min_value 갱신

    return min_value