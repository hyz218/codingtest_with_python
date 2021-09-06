#구현

#상하좌우
def directions_1():

    N = int(input())
    num_1, num_2 = 1,1 #초기화
    direction = input().split()

    for di in direction:
        if (di=='R'): 
            if (num_2<N-1): #오른쪽으로 이동할 수 있다면 이동
                num_2+=1
        elif (di=='L'): #왼쪽으로 이동할 수 있다면 이동
            if (num_2>1):
                num_2-=1
        elif (di=='U'): #위으로 이동할 수 있다면 이동
            if (num_1>1):
                num_1-=1
        else:
            if (num_1<N-1): #아래으로 이동할 수 있다면 이동
                num_1+=1

    return (num_1, num_2)

def directions_2():

    N = int(input())
    num_1, num_2 = 1,1
    direction = input().split()

    for di in direction:
        if ((di=='R') & (num_2<N-1)): #오른쪽으로 이동할 수 있다면 이동
            num_2+=1
        elif ((di=='L') & (num_2>1)): #왼쪽으로 이동할 수 있다면 이동
            num_2-=1
        elif ((di=='U')&(num_1>1)): #위으로 이동할 수 있다면 이동
            num_1-=1
        elif ((di=='D')&(num_1<N-1)): #아래으로 이동할 수 있다면 이동
            num_1+=1

    return (num_1, num_2)


#시각
def time_of_3():

    N=int(input())
    cnt = 0

    for i in range(N+1): #시간에 대한 반복문
        for m in range(60): #분에 대한 반복문
            for s in range(60): #초에 대한 반복문
                if '3' in (str(i)+str(m)+str(s)): #문자 중 3이 있으면 cnt 더하기
                    cnt+=1

    return cnt

#왕실의 나이트
def kingdom_of_knight():
    location = input()
    num_1 = int(ord(location[0]))-int(ord('a'))+1 #문자 -> 숫자로 변환
    num_2 = int(location[1])
    count = 0 

    knight = [(-2,-1),(-2,1),(-1,2),(-1,-2),(1,-2),(1,2),(2,1),(2,-1)] #knight가 이동할 수 있는 경우
    for k in knight:
        num_col = num_1 + k[0]
        num_row = num_2 + k[1]
        if (num_col>0 and num_col<9 and num_row>0 and num_col<9): #knight가 이동 가능한 범위에 해당하는지 판별
            count+=1

    return count

#게임 개발
def develop_game():
    n,m = map(int,input().split())
    mmap = []
    dx = [-1,0,1,0] #x축 이동 가능 방향
    dy = [0,1,0,-1] #y축 이동 가능 방향
    visit_map = [[0]*m for i in range(n)] #방문한 맵 초기화

    a, b, d = map(int,input().split()) #초기 위치와 방향
    for i in range(n):
        mmap.append(list(map(int,input().split()))) #맵 지정
    visit_map[a][b] = 1 #초기 위치 방문 설정

    count = 1 #방문한 맵의 갯수
    turn_time =0 #회전 횟수
    while True:
        d-=1 #왼쪽 방향으로 회전
        if(d==-1): #인덱스가 범위를 넘어가는 경우, 재지정
            d=3
        na = a+dx[d] #위치에서 해당 방향으로 변경(x축)
        nb = b+dy[d] #위치에서 해당 방향으로 변경(y축)

        if visit_map[na][nb]==0 and mmap[na][nb]==0: #방문하지 않은 map이면서, 방문 가능한 map인 경우
            visit_map[na][nb] = 1 #방문 맵에 추가
            a = na #위치 변경(x축)
            b = nb #위치 변경(y축)
            count+=1 #방문 횟수 더하기
            turn_time=0 #회전 횟수 초기화
        else:
            turn_time+=1 #왼쪽으로 회전
        if turn_time==4: #4 방향 모두 회전한 경우
            na = a-dx[d] #한칸 뒤로 위치 변경(x축)
            nb = b-dy[d] #한칸 뒤로 위치 변경(y축)
            if mmap[na][nb]==0: #방문이 가능한 map인 경우
                a=na #한칸 뒤 맵 방문을 위한 위치 변경(x축)
                b=nb #한칸 뒤 맵 방문을 위한 위치 변경(y축)
            else:
                break
            turn_time=0

    return count
