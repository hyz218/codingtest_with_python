def adventurer():
    n=int(input())
    data = list(map(int,input().split(' '))) #모험가의 정보 입력받기
    data.sort() #데이터를 오름차순으로 정렬하기

    result = 0 #총 그룹의 수 초기화
    count = 0 #현재 그룹에 포함된 모험가의 수 초기화

    for i in data:
        count+=1 #count 추가하기
        if count>=i: #모험가가 count보다 많거나 같은 경우
            result+=1 #result에 추가
            count=0 #count 0으로 초기화

    return result

#print(adventurer())

def multiple_or_plus():
    s = list(map(int,input()))

    for i in range(len(s)-1):
        if s[i]==0 or s[i]==1: #해당 숫자가 0이나 1인 경우 더하기
            s[i+1]=s[i]+s[i+1]
        else: #해당 숫자가 0이나 1이 아닌 경우 곱하기
            s[i+1]=s[i]*s[i+1]

    return s[-1] #제일 마지막에 있는 수 return

#print(multiple_or_plus())

def reverse_string():
    s = input()
    count0 = 0 #전부 0으로 바꾸는 경우
    count1 = 0 #전부 1로 바꾸는 경우

    if s[0]==0: #첫번째 숫자가 0인 경우 
        count1+=1 #1로 바뀌는 데에 추가
    else: #첫번째 숫자가 1인 경우 
        count0+=1 #0으로 바뀌는 데에 추가

    for i in range(len(s)-1): #s를 도는 반복문
        if s[i]!=s[i+1]: #해당 문자열과 다음 문자열이 다른 경우
            if s[i+1]==1: #다음 문자열이 1인 경우 0으로 바꾸는데에 추가
                count0+=1
            else: #다음 문자열이 0인 경우 1으로 바꾸는데에 추가
                count1+=1

    return min(count0,count1) #숫자를 바꾸는 경우 중 더 작은 값 return

#print(reverse_string())

def amount_cannot_make():
    n = int(input()) #동전의 갯수 입력받기
    amount = list(map(int,input().split(' '))) #동전 종류 입력받기
    amount.sort() #정렬
    target = 1 #target 초기화

    for i in amount: #동전을 도는 반복문
        if i>target: #i가 target보다 커지면 종료
            break
        target+=i

    return target

#print(amount_cannot_make())

def select_bowling_ball():
    n,m = map(int, input().split(' ')) #볼링공의 갯수 n, 공의 최대 무게 m 입력받기
    ball = list(map(int,input().split(' '))) #공의 무게 입력받기
    
    array = [0]*11 #무게별 공 초기화
    for x in ball: #무게에 해당하는 공의 갯수 count
        array[x]+=1

    result=0 #result 초기화
    for i in range(1,m+1):
        n-=array[i] #전체 갯수에서 해당 공의 갯수 빼기
        result+=array[i]*n #전체 갯수 * 해당 공의 갯수 더하기

    return result

#print(select_bowling_ball())

import heapq

def muzi_mukbang(food_times, k):
    if sum(food_times)<=k: #전체 시간을 합한 값이 k 보다 작으면 -1 return
        return -1
    
    q=[] #우선순위 큐 구현
    for i in range(len(food_times)): #시간의 길이까지 도는 반복문
        heapq.heappush(q,(food_times[i],i+1)) #시간과 번호를 q에 삽입
        
    sum_value = 0 #sum 값 초기화
    previous = 0 #직전에 다 먹은 음식의 시간
    length = len(food_times) #남은 음식의 갯수
    
    while sum_value+((q[0][0]-previous)*length)<=k: #sum_value + (현재 음식의 시간-이전 음식 시간)*현재 음식 개수와 k 비교
        now = heapq.heappop(q)[0]
        sum_value+=(now-previous)*length
        length-=1 #다 먹은 음식 제와
        previous=now #이전 음식 시간 재설정
        
    result = sorted(q,key=lambda x:x[1]) #남은 음식 중 몇번째 음식인지 확인하여 출력
    return result[(k-sum_value)%length][1]

#print(muzi_mukbang([3, 1, 2],5))