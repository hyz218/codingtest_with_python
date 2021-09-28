def fibo(x): #재귀적으로 구현한 피보나치 수열
    if x==1 or x==2: #x가 1이나 2면 1 반환
        return 1
    return fibo(x-1) + fibo(x-2)

#print(fibo(10))

def fibo_memoization(x): #메모이제이션을 적용한 피보나이제이션
    d=[0]*1000 #d 초기화
    def finonachi(x): #피보나치 수열
        if x==1 or x==2: #x가 1이나 2면 1 반환
            return 1
        if d[x]!=0: #d[x]에 이미 계산된 값이 있다면 그 값 반환
            return d[x]
        d[x] = finonachi(x-1) + finonachi(x-2) #d list에 계산 값 저장
        return d[x]

    return (finonachi(x))

#print(fibo_memoization(10))
#print(fibo_memoization(99))
    
def pibo_function():
    d = [0]*1000
    
    def pibo(x):
        print('f('+str(x)+')',end=' ') #재귀적으로 실행되는 과정 확인
        if x==1 or x==2: #x가 1이나 2면 1 반환
            return 1 
        if d[x]!=0: #d[x]에 이미 계산된 값이 있다면 그 값 반환
            return d[x]
        d[x] = pibo(x-1)+pibo(x-2) #d list에 계산 값 저장
        return d[x]

    return pibo(6)

#print(pibo_function())

def fibonachi_bottom_up(num):
    d = [0]*100 #d list 초기화
    d[1] = 1 #d[1] 초기화
    d[2] = 1 #d[2] 초기화
    n=99

    for i in range(3,n+1):
        d[i] = d[i-1] + d[i-2] # d[i]에 해당하는 값 저장

    return d[num]