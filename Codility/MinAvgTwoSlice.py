def solution(A): #O(N ** 3)
    min_value = 1e9
    min_index = 1e9
    for i in range(len(A)-1):
        for j in range(i+1,len(A)):
            if sum(A[i:j+1])/(j-i+1) < min_value:
                min_value = sum(A[i:j+1])/(j-i+1)
                min_index = i

    return min_index