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


