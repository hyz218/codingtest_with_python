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

def make_one(): #Using bottom-up dynamic programming
    x = int(input()) #x 입력받기
    
    d=[0]*100000 #DP table 초기화

    for i in range(2,x+1): #점화식 활용 Dynamic programming
        d[i] = d[i-1]+1 #현재의 수에서 1을 빼는 경우
        if i%2 == 0: #i가 2로 나누어 떨어지는 경우
            d[i] = min(d[i],d[i//2]+1)
        if i%3 == 0: #i가 3으로 나누어 떨어지는 경우
            d[i] = min(d[i],d[i//3]+1)
        if i%5 == 0: #i가 5로 나누어 떨어지는 경우
            d[i] = min(d[i],d[i//5]+1)
    
    return d[x]

#print(make_one())

def ant_fighter(): 
    n=int(input()) #정수 n 입력받기
    array = list(map(int,input().split())) #모든 식량 정보 입력받기

    d = [0]*1000 #DP테이블 초기화

    #점화식 활용 Dynamic programming
    d[0] = array[0]
    d[1] = max(array[0],array[1])
    for i in range(2,n):
        d[i] = max(d[i-1],d[i-2]+array[i]) #현재 위치에서 전 것과 전전것+현재위치 중 max값

    return(d[n-1]) #n만큼 있는거니까 n-1

#print(ant_fighter())

def floor_work(): #바닥공사 
    n = int(input()) #가로의 길이 n 입력받기
    d = [0]*1001 #점화식 활용 Dynamic programming

    d[1] = 1 #1*2를 채우는 경우의 수
    d[2] = 3 #2*2를 채우는 경우의 수
    for i in range(3,n+1):
        d[i] = (d[i-1] +2*d[i-2]% 796796) #점화식 ai = a(i-1) + 2 * a(i-2)

    return d[n]

#print(floor_work())

def money_component(): #효율적인 화폐 구성
    N, M = map(int,input().split()) #화폐의 종류의 갯수 / 구성해야하는 금액 입력받기
    list_n = [] #list 초기화
    
    for i in range(N):
        list_n.append(int(input())) #화폐 단위 입력받기

    d = [10001]*(M+1) #점화식 활용 Dynamic programming

    d[0]=0 #0원 초기화
    for i in range(N): #화폐 단위의 갯수만큼 도는 반복문
        for j in range(list_n[i],M+1): #금액까지 도는 반복문
            if d[j-list_n[i]] != 10001: #해당하는 금액을 만들 수 있는 경우
                d[j] = min(d[j],d[j-list_n[i]]+1) #더 작은 값으로 갱신


    if d[M] == 10001: #해당 금액을 만들 수 없는 경우 
        return -1 #-1 반환
    
    return d[M] #해당 금액을 만들 수 있는 경우 최소 갯수 반환

#print(money_component())