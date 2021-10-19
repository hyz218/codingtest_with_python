from collections import deque

def find_length_city():
    N,M,K,X = map(int,input().split(' ')) #도시갯수, 도로 갯수, 거리정보, 출발도시번호 입력받기
    graph = [[] for _ in range(N+1)] #그래프 초기화

    for _ in range(M):
        a,b = map(int,input().split(' '))
        graph[a].append(b)

    distance = [-1]*(N+1) #모든 도시에 대한 최단 거리 초기화
    distance[X] = 0 #출발 도시까지의 거리는 0으로 설정

    q=deque([X]) #BFS 실행
    while q:
        now = q.popleft()
        for next_node in graph[now]: #현재 도시에서 이동할 수 있는 모든 도시 확인
            if distance[next_node] == -1: #아직 방문하지 않은 도시라면
                distance[next_node] = distance[now]+1
                q.append(next_node)

    check = False
    for i in range(1,N+1): #최단 거리가 K인 모든 도시 번호를 오름차순으로 출력
        if distance[i]==K:
            print(i)
            check = True
    
    if check== False: #최단 거리가 K인 도시가 없다면 -1 출력
        print(-1)

#find_length_city()

# def research_center():
#     N,M = map(int, input().split(' '))
#     data = [] #초기 맵 리스트
#     temp = [[0]*M for _ in range(N)] #벽을 설치한 뒤의 맵 리스트

#     for _ in range(N):
#         data.append(list(map(int, input().split(' '))))

#     dx = [-1,0,1,0] #4가지 이동 방향에 대한 리스트
#     dy = [0,1,0,-1]

#     result = 0

#     def virus(x,y):
#         for i in range(4):
#             nx = x+dx[i]
#             ny = y+dy[i]
#             if nx>=0 and nx< N and ny>=0 and ny<M: #상하좌우로 바이러스 퍼질 수 있는 경우
#                 if temp[nx][ny] == 0: #해당 위치에 바이러스를 배치시키고 재귀적 실행
#                     temp[nx]=2
#                     virus(nx,ny)

#     def get_score(): #현재 맵에서 안전영역의 크기를 계산하는 함수
#         score = 0 #score 초기화
#         for i in range(N):
#             for j in range(M):
#                 if temp[i][j]==0:
#                     score+=1

#         return score

#     def dfs(count): #깊이 우선 탐색을 이용해 울타리를 설치하면서 매번 안전 영역의 크기 계산
#         global result
#         #울타리가 3개 설치된 경우
#         if count==3:
#             for i in range(N):
#                 for j in range(M):
#                     temp[i][j] = data[i][j]
#             #각 바이러스의 위치에서 전파 진행
#             for i in range(N):
#                 for j in range(M):
#                     if temp[i][j]==2:
#                         virus(i,j)
#             result = max(result,get_score)
#             return
#         #빈 공간에 울타리 설치하기
#         for i in range(N):
#             for j in range(M):
#                 if data[i][j]==0:
#                     data[i][j]=1
#                     count+=1
#                     dfs(count)
#                     data[i][j]=0
#                     count-=1

#     dfs(0)

#     print(result)

# research_center()

def convert_Parenthesis():
    def balance_index(p): #균형잡힌 괄호 문자열 인덱스 반환
        count = 0 #왼쪽 괄호의 갯수
        for i in range(len(p)):
            if p[i]=='(':
                count+=1
            else: 
                count-=1
            if count==0:
                return i
        
    def check_proper(p): #올바른 괄호 문자열 판단
        count = 0
        for i in p:
            if i=='(':
                count+=1
            else:
                if count==0: #쌍이 맞지 않는 경우 False 반환
                    return False
                count-=1
        return True

    def solution(p):
        answer = ''
        if p=='':
            return answer
        index = balance_index(p)
        u = p[:index+1]
        v = p[index+1:]
        #올바른 괄호 문자열이면 v에 함수 결과 붙여서 반환
        if check_proper(u):
            answer = u+solution(v)
        else: #아니라면 아래 과정 수행
            answer = '('
            answer+=solution(v)
            answer+=')'
            u=list(u[1:-1])
            for i in range(len(u)):
                if u[i]=='(':
                    u[i]=')'
                else:
                    u[i]='('
            answer+="".join(u)
            
        return answer

    return print(solution('()))((('))

from collections import deque
def fight_infection():
    N,K = map(int,input().split(' '))

    graph = [] #전체 보드 정보를 담는 리스트
    data = [] #바이러스 정보를 담는 리스트

    for i in range(N):
        graph.append(list(map(int, input().split(' ')))) #보드를 줄 단위로 입력받기
        for j in range(N):
            if graph[i][j]!=0: #해당 위치에 바이러스가 존재하는 경우
                data.append((graph[i],0,i,j))
    
    data.sort()
    q = deque(data)

    target_s, target_x, target_y = map(int,input().split(' '))

    dx = [-1,0,1,0] #바이러스가 퍼져나갈 수 있는 4가지 위치
    dy = [0,1,0,-1]

    while q: #너비 우선 탐색 진행
        virus, s, x, y = q.popleft()
        if s==target_s: #정확히 s초가 지나거나, 큐가 빌 때 까지 반복
            break
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx and nx<N and 0>=ny and ny<N: #아직 방문하지 않은 위치라면 그 위치에 바이러스 넣기
                if graph[nx][ny] == 0:
                    graph[nx][ny] = virus
                    q.append((virus,s+1,nx,ny))

    return graph[target_x-1][target_y-1]

#print(fight_infection())