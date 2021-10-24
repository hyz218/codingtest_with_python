# def solution(A):    -> O(n*n)
#     min_value=1e9
#     for i in range(len(A)-1):
#         min_value = min(min_value, abs(sum(A[:i])-sum(A[i+1:])))
#     return min_value


def solution(A): #O(n)
    left_side = 0 #왼쪽 부분 초기화
    right_side = sum(A) #오른쪽 부분 초기화
    min_value = 1e9 #min값 초기화

    for i in range(len(A)-1): #A의 길이-1까지 도는 반복문
        left_side+=A[i] #왼쪽 부분 A[i]에 해당하는 원소 더하기
        right_side-=A[i] #오른쪽 부분에 A[i]에 해당하는 원소 빼기
        min_value = min(min_value,abs(left_side-right_side)) #왼쪽 부분에서 오른쪽 부분을 뺀 값에 절대값을 취한 후 min_value와 비교하여 더 작은값 return

    return min_value