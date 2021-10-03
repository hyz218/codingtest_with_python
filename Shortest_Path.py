import sys

def simple_Dijkstra():
    #간단한 Dijkstra 알고리즘 구현
    input = sys.stdin.readline #입력을 치환해서 적용
    INF = int(1e9) #무한 값으로 10억 설정

    n, m = map(int,input().split()) #노드의 개수, 간선의 개수 입력받기
    start = int(input()) #시작 노드 입력받기
    graph = [[] for i in range(n+1)] #각 노드에 연결된 노드 정보 graph 생성
    visited = [False]*(n+1) #방문여부 초기화
    distance = [INF]*(n+1) #거리 무한 값으로 초기화

    for _ in range(m): #모든 간선의 정보 입력받기
        a, b, c = map(int,input().split())
        graph[a].append((b,c)) #a번 노드에서 b번 노드로 가는 비용이 c라는 의미

    def get_smallest_node(): #방문하지 않은 노드 중 최단 거리가 짧은 노드의 번호 반환
        min_value = INF #value 무한 값으로 초기화
        index = 0 #index 초기화
        for i in range(1,n+1): #간선을 도는 반복문
            if distance[i]< min_value and not visited[i]: #거리가 가장 짧고 간선을 아직 방문하지 않은 경우 
                min_value = distance[i] #min_value에 저장
                index = i #index 저장
        return index #index 반환

    def dijkstra(start): #다익스트라 알고리즘
        distance[start] = 0 #시작 노드 거리 초기화
        visited[start] = True #방문 기록 남기기
        for j in graph[start]: #그래프에 start 노드에 해당하는 값을 도는 반복문
            distance[j[0]] = j[1] #다른 노드로 가는 거리(비용)를 저장
        for i in range(n-1):
            now = get_smallest_node() #방문하지 않은 노드 중 최단 거리가 짧은 노드의 번호 받기
            visited[now] = True #now에 대해 방문 기록 남기기
            for j in graph[now]: #now를 기준으로 도는 반복문
                cost = distance[now] + j[1] #현재 노드에서의 거리 계산
                if cost<distance[j[0]]: #현재 노드를 거쳐서 다른 노드로 이동하는 거리가 짧은 경우
                    distance[j[0]] = cost #cost 업데이트

    dijkstra(start) #다익스트라 알고리즘 수행

    for i in range(1, n+1): #모든 노드를 도는 반복문
        if distance[i] == INF: #해당 노드에서 갈 수 없는 경우 무한 값 반환
            print("INFINITY")
        else: #최단경로 출력
            print(distance[i])

    return distance

#simple_Dijkstra()

import heapq
import sys

def improved_dijkstra(): #개선된 다익스트라 알고리즘 
    input = sys.stdin.readline #input 선언
    INF = int(1e9) #무한값 선언

    n, m = map(int,input().split()) #노드 갯수와 간선 갯수 입력받기
    start = int(input()) #시작 노드 입력받기
    graph = [[] for i in range(n+1)] #각 노드에 연결된 노드 정보 graph 생성
    distance = [INF]*(n+1) #거리 무한 값으로 초기화

    for _ in range(m): #모든 간선의 정보 입력받기
        a,b,c = map(int,input().split())
        graph[a].append((b,c)) #a번 노드에서 b번 노드로 가는 비용이 c라는 의미

    def dijkstra(start):
        q = [] #큐 초기화
        heapq.heappush(q,(0,start)) #시작 노드로 가기 위한 최단 경로를 0으로 초기화하여 큐에 삽입
        distance[start] = 0 #거리 0으로 초기화
        while q: #큐가 비어있지않다면 반복
            dist,now = heapq.heappop(q) #큐에 저장 최단거리가 짧은 거리와 현재 노드 꺼내기
            if distance[now]<dist: #노드가 이미 처리되었다면 무시
                continue
            for i in graph[now]: #현재 노드와 연결된 인접 노드들 확인
                cost = dist + i[1] #거리 계산
                if cost < distance[i[0]]: #현재 노드를 거쳐서 다른 노드로 이동하는 거리가 짧은 경우
                    distance[i[0]] = cost  #cost 업데이트
                    heapq.heappush(q,(cost,i[0])) #q에 추가하기

    dijkstra(start) #다익스트라 알고리즘 수행

    for i in range(1,n+1):
            if distance[i] == INF: #해당 노드에서 갈 수 없는 경우 무한 값 반환
                print("INFINITY")
            else: #최단경로 출력
                print(distance[i])

    return distance

#improved_dijkstra()

def floyd_warshall():
    INF = int(1e9) #무한 값 설정

    n=int(input()) #노드 갯수 입력받기
    m=int(input()) #간선 갯수 입력받기

    graph = [[INF]*(n+1) for _ in range(n+1)] #2차원 리스트(graph 표현)를 만들고, 모든 값을 무한 값으로 초기화

    for a in range(1,n+1): #자기 자신에서 자기자신으로 가는 cost 0으로 초기화
        for b in range(1,n+1):
            if a==b:
                graph[a][b]=0

    for _ in range(m): #간선의 정보를 입력받아 초기화
        a,b,c = map(int,input().split())
        graph[a][b] = c

    for k in range(1,n+1): #점화식에 따라 플로이드 워셜 알고리즘 수행
        for a in range(1,n+1):
            for b in range(1,n+1):
                graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

    for a in range(1,n+1): #수행된 결과 출력
        for b in range(1,n+1):
            if graph[a][b] == INF: #갈 수 없는 경우 "INFINITY" 출력
                print("INFINITY", end = " ")
            else: #최단 거리 출력
                print(graph[a][b], end=" ")

        print()

    return graph

#floyd_warshall()