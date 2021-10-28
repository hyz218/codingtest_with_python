def solution(A): #O(N * log(N))
    A.sort() #array를 오름차순으로 정렬하기
    return max(A[0]*A[1]*A[-1],A[-1]*A[-2]*A[-3]) #음수가 있는 경우, -*-는 + 이므로 음수를 없애주기 위한 A[0]*A[1]에 가장 큰 수를 곱한 값과 가장 큰 값 3개를 그대로 곱한 값을 비교해서 더 큰 값 return
