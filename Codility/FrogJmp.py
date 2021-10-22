def solution(X, Y, D):
    Y-=X #초기 X값 빼주기 
    if Y%D==0: #Y가 D로 나누어떨어지는 경우 나눈 값 return
        num = Y//D
    else: #Y가 D로 나누어떨어지지 않는 경우 나눈 값 +1 return
        num = Y//D+1
    return num