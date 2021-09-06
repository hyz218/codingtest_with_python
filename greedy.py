#greedy

# 거스름돈
def change(n):
    coin_count = 0
    coin_type = [500,100,50,10] #coin 종류 list

    for c in coin_type:
        coin_count += n//c #//나눗셈 연산 시 소수점 이하 수 버리기
        n%=c #n 변경

    return coin_count

#큰 수의 법칙
def law_of_large_number():
    n,m,k = map(int,input().split())
    data = list(map(int,input().split()))
    num = 0

    data.sort() #오름차순 정렬
    max_num_1 = data[n-1] #가장 큰 수
    max_num_2 = data[n-2] #두번째로 큰 수

    for i in range(m):
        if((i+1)%k==0):
            num+=max_num_2 #k번 연속으로 숫자 입력이 불가능 하므로 두번째로 큰 수 더하기
        else:
            num+=max_num_1 #가장 큰 수 더하기

    return num

#숫자 카드 게임
def card_game_1():
    num = 0
    min_num = 0
    n,m = map(int,input().split())

    for i in range(n):
        list_num = list(map(int,input().split()))
        min_num = min(list_num) #행 중 작은 수 구하기
        if (min_num>num): #구한 작은 수가 원래 가진 수 보다 크면 업데이트
            num = min_num

    return num

def card_game_2():
    min_num = []
    n,m = map(int,input().split())
    for i in range(n):
        list_num = list(map(int,input().split()))
        min_num.append(min(list_num)) # 행 중 작은 수 구하기
    
    return max(min_num) #작은 수 리스트 중 가장 큰 값 return 

#1이 될 때까지
def until_one():
    N,K = map(int,input().split())
    num=0
    while True:
        if (N==1): #N이 1이 되면 반복문 빠져나오기
            break
        if (N%K==0): #N이 K로 나뉘어 떨어지면 나누기
            num+=1
            N/=K
        else: #N이 K로 나뉘어 떨어지지 않는 경우 -1
            N-=1 
            num+=1

    return num