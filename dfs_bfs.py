#인접 행렬
def adjacency_matrix():
    INF = 99999999
    graph = [
        [0,7,5],
        [7,0,INF],
        [5,INF,0]
    ]

#인접 리스트
def adjacency_list():
    graph = [[] for _ in range(3)]

    graph[0].append((1,7))
    graph[0].append((2,5))

    graph[1].append((0,7))
    graph[2].append((0,5))

    return graph

def dfs(graph,v,visited):
    #현재 노드 방문 처리
    visited[v] = True
    print(v,end=' ')
    #현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)


def dfs_ex():
    graph = [
        [],
        [2,3,8],
        [1,7],
        [1,4,5],
        [3,5],
        [3,4],
        [7],
        [2,6,8],
        [1,7]]

    visited = [False]*9

    dfs(graph,1,visited)

from collections import deque

def bfs(graph,start,visited):
    #큐 구현을 위한 라이브러리 사용
    queue = deque([start])
    #현재 노드를 방문 처리
    visited[start] = True
    #큐가 빌 때까지 반복
    while queue:
        #큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v,end=' ')
        #해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

def bfs_ex():

    graph = [
        [],
        [2,3,8],
        [1,7],
        [1,4,5],
        [3,5],
        [3,4],
        [7],
        [2,6,8],
        [1,7]
    ]

    visited = [False] * 9
    bfs(graph,1,visited)



#DFS
#음료수 얼려 먹기
def freeze_beverage():
    N,M = map(int,input().split())

    graph = []
    for i in range(N):
        graph.append(list(map(int,input())))

    def dfs(x,y): #DFS
        if x<=-1 or x>=N or y<=-1 or y>=M: #범위를 벗어나면 종료
            return False
        if graph[x][y]==0: #해당 노드를 방문하지 않았다면
            graph[x][y] = 1 #해당 노드 방문 처리
            #상하좌우 재귀적 호출
            dfs(x-1,y)
            dfs(x,y-1)
            dfs(x+1,y)
            dfs(x,y+1)
            return True
        return False

    result = 0
    for i in range(N):
        for j in range(M):
            if dfs(i,j) == True:
                result+=1

    return result


#BFS
#미로탈출

from collections import deque #큐를 사용하기 위한 라이브러리 load

def maze():
    n,m = map(int,input().split())
    
    graph = []
    for i in range(n):
        graph.append(list(map(int,input())))
        
    dx = [-1,1,0,0] #상하좌우 방향
    dy = [0,0,-1,1]
    
    def bfs(x,y):
        queue = deque() #큐 구현을 위한 deque 라이브러리 사용
        queue.append((x,y)) 
        
        while queue: #큐가 빌 때 까지 반복
            x,y = queue.popleft()
            
            for i in range(4): #네 방향으로 위치 확인
                nx = x+dx[i]
                ny = y+dy[i]
                
                if nx<0 or ny<0 or nx>=n or ny>=m: #공간을 벗어난 경우 무시
                    continue
                if graph[nx][ny]==0: #벽인 경우 무시
                    continue
                if graph[nx][ny]==1: #해당 노드를 처음 방문하는 경우 최단거리 기록
                    graph[nx][ny]=graph[x][y] + 1 #방문 표시
                    queue.append((nx,ny)) #추가하기
        return graph[n-1][m-1] #가장 오른쪽 아래까지의 최단거리 반환  
    
    return bfs(0,0)#현재 위치에서 BFS 수행