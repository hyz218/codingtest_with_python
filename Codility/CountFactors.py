def solution(N): # O(N)
    if N==1:
        return 1

    nums = 2
    for i in range(2,N):
        if N%i==0:
            nums+=1

    return nums