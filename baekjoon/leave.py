def leave():
    n=int(input())
    t,p=[0]*n, [0]*n

    for i in range(n):
        t[i],p[i] = map(int,input().split(' '))
    
    dp = [0 for i in range(n+1)] #dp list 생성

    for i in range(n-1,-1,-1): #끝에서부터 도는 반복문
        if i + t[i] > n: #날짜가 넘어가는 경우
            dp[i] = dp[i+1] #뒤에 있는 값을 앞으로 가져오기
        else: #날짜가 넘어가지 않는 경우
            dp[i] = max(p[i] + dp[i + t[i]], dp[i+1]) #뒤에 있는 값과 새로 계산한 cost를 비교해 큰 값 취하기
                
    return dp[0]

#print(leave())