# A binary gap 

def solution(N):
    n = str(bin(N))
    num = list(map(int,n[2:]))
    max_cnt=0
    cnt=0

    for i in range(len(num)-1):
        if num[i+1]==0:
            cnt+=1
        if num[i+1]==1:
            max_cnt = max(cnt,max_cnt)
            cnt=0

    return max_cnt