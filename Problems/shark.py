from collections import deque

def baby_shark():
    INF = 1e9 #무한 값 10억 설정

    N=int(input()) #맵의 크기 N 입력받기

    array = [] #전체 모든 칸에 대한 정보 입력
    for i in range(N):
        array.append(list(map(int,input().split(' '))))

    now_size = 2 #아기 상어의 현재 크기 변수와 위치 변수
    now_x, now_y = 0, 0

    for i in range(N): #아기 상어의 시작 위치를 찾은 후 그 위치에 아무것도 없다고 처리
        for j in range(N):
            if array[i][j] == 9:
                now_x, now_y = i,j
                array[now_x][now_y] = 0

    dx = [-1,0,1,0]
    dy = [0,-1,0,1]

    def bfs(): #모든 위치까지의 최단 거리만 계산하는 bfs 함수
        #값이 -1이라면 도달할 수 없다는 의미(초기화)
        dist = [[-1]*N for _ in range(N)]
        #시작 위치는 도달 가능하다고 보며 거리는 0
        q=deque([(now_x,now_y)])
        dist[now_x][now_y] = 0
        while q:
            x,y = q.popleft()
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                if 0<=nx and nx<N and 0<=ny and ny<N:
                    if dist[nx][ny]==-1 and array[nx][ny]<=now_size: #자신의 크기보다 작거나 같은 경우 지나갈 수 있음
                        dist[nx][ny] = dist[x][y]+1
                        q.append((nx,ny))
        return dist

    def find(dist): #최단 거리 테이블이 주어졌을 때 먹을 물고기를 찾는 함수
        x,y = 0,0
        min_dist = INF
        for i in range(N):
            for j in range(N):
                #도달 가능하면서 먹을 수 있는 물고기일 때
                if dist[i][j]!=-1 and 1<=array[i][j] and array[i][j]<now_size:
                    #가장 가까운 물고기 1마리만 선택
                    if dist[i][j]<min_dist:
                        x,y = i,j
                        min_dist = dist[i][j]
        if min_dist == INF: #먹을 수 있는 물고기가 없는 경우
            return None
        else:
            return x,y,min_dist
    
    result = 0 #최종 답안
    ate = 0 #현재 크기에서 먹은 양

    while True:
        #먹을 수 있는 물고기의 위치 찾기
        value = find(bfs())
        #먹을 수 있는 물고기가 없는 경우 현재까지 움직인 거리 출력
        if value == None:
            print(result)
            break
        else:
            #현재 위치 갱신 및 이동거리 변경
            now_x, now_y = value[0], value[1]
            result+=value[2]
            #먹은 위치에는 이제 아무것도 없도록 처리
            array[now_x][now_y] = 0
            ate+=1
            #자신의 현재 크기 이상으로 먹은 경우, 크기 증가
            if ate>=now_size:
                now_size+=1
                ate=0

    return result

#baby_shark()

#def teenager