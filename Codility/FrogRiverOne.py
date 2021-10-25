def solution(X, A):
    leaf = [0] * X #left를 0으로 초기화
    check_sum = 0 #check_sum을 0으로 초기화
    for i in range(len(A)):
        if leaf[A[i]-1]==0: #방문한 적 없다면 1로 변경 후 check_sum 추가
            leaf[A[i]-1] = 1
            check_sum+=1
        if check_sum==X: #방문횟수와 X가 같아지면 i 반환
            return i

    return -1 #조건을 채우지 못한 경우 -1 반환