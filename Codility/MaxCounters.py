#def solution(N, A): #O(N*M)
#    array = [0 for i in range(N)]
#    for i in range(len(A)):
#        if A[i]==N+1:
#            array = [max(array) for _ in range(len(array))]
#        else:
#            array[A[i]-1]+=1
#
#    return array