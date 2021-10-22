#CyclicRotation
def solution(A, K):

    if A==[] or K==len(A): #if the list is empty or same to the last result of function
        return A

    for i in range(K):
        A.insert(0,A[-1])
        A.pop()

    return A