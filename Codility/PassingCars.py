def solution(A): #O(N)
    east_cnt = 0 #동쪽으로 가는 차의 갯수 초기화
    passing_car = 0 #pair 초기화
    for i in range(len(A)): #A를 도는 반복문
        if A[i]==0: #A가 동쪽으로 가는 경우 +1
            east_cnt+=1
        else: #A가 서쪽으로 가는 경우 동쪽으로 가는 차의 수 더하기
            passing_car+=east_cnt
        
        if passing_car>1000000000: #pair 수가 1000000000를 초과하면 -1 반환
            return -1

    return passing_car #아닌 경우 pair의 수 반환