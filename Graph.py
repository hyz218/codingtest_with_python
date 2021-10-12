def coprime(): #서로소 집합 알고리즘
    def find_parent(parent,x): #특정 원소가 속한 집합 찾기
        if parent[x]!=x: #루트 노드가 아니면 루트 노드를 찾을 때 까지 재귀로 호출
            return find_parent(parent,parent[x])
        return x

    def union_parent(parent,a,b): #두 원소가 속한 집합 합치기
        a = find_parent(parent,a)
        b = find_parent(parent,b)
        if a<b: #작은 수가 parent가 되도록 만들기
            parent[b] = a
        else:
            parent[a] = b

    v,e = map(int,input().split(' ')) #노드의 갯수와 간선의 갯수 입력받기
    parent = [0] * (v+1) #부모 list 초기화

    for i in range(1,v+1):  #부모list에서 부모를 자기 자신으로 초기화
        parent[i]=i

    for i in range(e):
        a,b = map(int, input().split(' ')) #union 연산 수행
        union_parent(parent,a,b)

    print('각 원소가 속한 집합: ', end='')
    for i in range(1,v+1):
        print(find_parent(parent,i),end=' ')

    print()

    print('부모 테이블: ',end='')
    for i in range(1,v+1):
        print(parent[i],end=' ')

    return parent

#coprime()

def improved_coprime(): #개선된 서로소 집합 알고리즘
    def find_parent(parent,x):
        if parent[x]!=x: #루트 노드가 아니면 루트 노드를 찾을 때 까지 재귀로 호출
            parent[x] = find_parent(parent,parent[x])
        return parent[x]

    def union_parent(parent,a,b): #두 원소가 속한 집합 합치기
        a = find_parent(parent,a)
        b = find_parent(parent,b)
        if a<b: #작은 수가 parent가 되도록 만들기
            parent[b] = a
        else:
            parent[a] = b

    v,e = map(int,input().split(' ')) #노드의 갯수와 간선의 갯수 입력받기
    parent = [0] * (v+1) #부모 list 초기화

    for i in range(1,v+1):  #부모list에서 부모를 자기 자신으로 초기화
        parent[i]=i

    for i in range(e):
        a,b = map(int, input().split(' ')) #union 연산 수행
        union_parent(parent,a,b)

    print('각 원소가 속한 집합: ', end='')
    for i in range(1,v+1):
        print(find_parent(parent,i),end=' ')

    print()

    print('부모 테이블: ',end='')
    for i in range(1,v+1):
        print(parent[i],end=' ')

    return parent

#improved_coprime()

def cycle_by_coprime(): #특정 원소가 속한 집합을 찾기
    def find_parent(parent,x): 
        if parent[x]!=x: #루트 노드가 아니면 재귀적 호출 
            parent[x] = find_parent(parent,parent[x])
        return parent[x]

    def union_parent(parent,a,b): #두 원소가 속한 집합 합치기
        a = find_parent(parent,a)
        b = find_parent(parent,b)
        if a<b:
            parent[b] = a
        else:
            parent[a] = b
    
    v, e = map(int,input().split(' ')) #노드의 갯수와 간선의 갯수 입력받기
    parent = [0]*(v+1) #부모 테이블 초기화

    for i in range(1,v+1): #부모 테이블 자기 자신으로 초기화
        parent[i]=i

    cycle = False #cycle 초기화

    for i in range(e):
        a,b = map(int,input().split())
        if find_parent(parent,a)==find_parent(parent,b): #사이클이 발생한 경우 종료
            cycle = True
            break
        else: #사이클이 발생하지 않은 경우 합집합 수행
            union_parent(parent,a,b)

    if cycle:
        print("사이클 발생")
    else:
        print("사이클 미발생")

    return cycle

#cycle_by_coprime()

def kruskal():
    def find_parent(parent,x): 
        if parent[x]!=x: #루트 노드가 아니면 재귀적 호출 
            parent[x] = find_parent(parent,parent[x])
        return parent[x]

    def union_parent(parent,a,b): #두 원소가 속한 집합 합치기
        a = find_parent(parent,a)
        b = find_parent(parent,b)
        if a<b:
            parent[b] = a
        else:
            parent[a] = b
    
    v, e = map(int,input().split(' ')) #노드의 갯수와 간선의 갯수 입력받기
    parent = [0]*(v+1) #부모 테이블 초기화

    edges = [] #모든 간선을 담을 리스트와 최종 비용을 담을 변수 초기화
    result = 0

    for i in range(1,v+1): #부모 테이블에서 부모를 자기 자신으로 초기화
        parent[i] = i

    for _ in range(e): #간선에 대한 정보 입력받기
        a,b,cost = map(int,input().split(' '))
        edges.append((cost,a,b))

    edges.sort() #비용 순으로 정렬

    for edge in edges:
        cost, a, b = edge
        if find_parent(parent,a) != find_parent(parent,b): #사이클이 발생하지 않는 경우에만 집합에 포함
            union_parent(parent,a,b)
            result+=cost

    print(result)

    return result

#kruskal()

from collections import deque
def topology(): #위상정렬
    v,e = map(int, input().split(' ')) #노드의 개수와 간선의 개수 입력받기
    indegree = [0]*(v+1) #모든 노드의 진입차수 0으로 초기화
    graph = [[] for i in range(v+1)] #각 노드에 연결된 간선 정보를 담기 위한 그래프 초기화

    for _ in range(e): #간선 정보 입력받기
        a,b = map(int, input().split(' '))
        graph[a].append(b) #정점 a에서 b로 이동가능
        indegree[b]+=1 #b의 진입차수 증가

    def topology_sort(): #위상 정렬 함수
        result=[] #알고리즘 수행 결과를 담는 리스트 초기화
        q=deque() #deque 라이브러리 사용

        for i in range(1,v+1): #진입차수가 0인 노드를 큐에 삽입
            if indegree[i]==0:
                q.append(i)

        while q: #q가 있는 경우 반복
            now = q.popleft() #q에서 원소 꺼내기
            result.append(now) #result에 삽입하기

            for i in graph[now]: #해당 원소와 연결된 노드들의 진입차수 -1하기
                indegree[i]-=1
                if indegree[i]==0: #새로 진입차수가 0이 되는 노드 큐에 삽입하기
                    q.append(i) 

        for i in result: #위상정렬 수행 결과 출력
            print(i,end=' ')

    return topology_sort()

#topology()