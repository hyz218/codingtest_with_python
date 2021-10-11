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

