def lucky_straight():
    N = list(map(str,input())) #문자열을 list로 받기 
    length = len(N)//2 #길이를 반으로 나누기
    N = list(map(int,N)) #list 안의 인자를 int로 변경하기
    N_left = N[:length] #list의 왼쪽 부분만 저장
    N_right = N[length:] #list의 오른쪽 부분만 저장
    if sum(N_left)==sum(N_right): #왼쪽부분과 오른쪽 부분의 합이 같다면 LUCKY return
        return "LUCKY" 

    return "READY" #다르면 READY return

#print(lucky_straight())

def rearrange_string():
    s = list(input())
    result = []
    num = 0
    s.sort()

    for x in s:
        if x.isalpha():
            result.append(x)
        else:
            num+=int(x)
    
    result.append(str(num))

    return "".join(result)

#print(rearrange_string())

def string_compression():
    s=input()
    answer = len(s) #answer를 문자의 총 길이로 초기화
    for step in range(1,len(s)//2+1): #1부터 문자열 길이의 반+1까지 반복
        compressed = "" #문장 초기화
        prev = s[0:step] #초기 문자열 지정
        count = 1 #초기 문자의 count지정
        for i in range(step,len(s),step): #해당 단위를 늘리며 확인
            if prev == s[i:i+step]: #이전 문자열과 해당 문자열이 같을 경우
                count+=1 #count 추가
            else:
                if count>=2: #count가 2가 넘는 경우
                    compressed+=str(count)+prev #숫자와 문자열 넣기
                else: #count가 1인경우
                    compressed+=  prev #문자열 넣기
                prev = s[i:i+step] #문자열 초기화
                count=1 #count초기화
        if count>=2: #남아있는 문자열 확인하기
            compressed+=str(count)+prev 
        else:
            compressed+=prev
        answer = min(answer,len(compressed)) #문자열의 길이가 가장 짧은 것 채택

    return answer

#print(string_compression())

def Lock_and_key():

    def rotate_a_matrix_by_90_degree(a): #2차원 리스트 90도 회전
        n=len(a)
        m=len(a[0])
        result = [[0]*n for _ in range(m)] #결과 리스트
        for i in range(n):
            for j in range(m):
                result[j][n-i-1] = a[i][j]
        return result

    def check(new_lock): #자물쇠의 중간 부분이 모두 1인지 확인
        lock_length = len(new_lock)//3
        for i in range(lock_length,lock_length*2):
            for j in range(lock_length,lock_length*2):
                if new_lock[i][j]!=1:
                    return False
        return True

    def solution(key, lock):
        answer = True
        n=len(lock)
        m=len(key)
        
        new_lock = [[0]*(n*3) for _ in range(n*3)] #자물쇠의 크기를 기존의 3배로 변환
        for i in range(n): #새로운 자물쇠 중앙 부분에 기존 자물쇠 넣기
            for j in range(n):
                new_lock[i+n][j+n]=lock[i][j]
        
        for rotation in range(4): #4가지 방향에 대해서 확인
            key = rotate_a_matrix_by_90_degree(key) #열쇠 회전
            for x in range(n*2):
                for y in range(n*2):
                    for i in range(m): #자물쇠에 열쇠 끼워넣기
                        for j in range(m):
                            new_lock[x+i][y+j]+=key[i][j]
                    if check(new_lock)==True: #새로운 자물쇠에 열쇠가 정확히 들어맞는지 검사
                        return True
                    for i in range(m): #자물쇠에서 열쇠를 다시 빼기
                        for j in range(m):
                            new_lock[x+i][y+j] -=key[i][j]
        return False
    
    return solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]])

#print(Lock_and_key())

def snake():
    N = int(input())
    K = int(input())
    data = [[0]*(N+1) for _ in range(N+1)] #맵 정보
    info = [] #방향 회전 정보
    for i in range(K): #맵 정보(사과가 있는 곳 1로 표시)
        a,b = map(int,input().split())
        data[a][b] = 1
    
    l=int(input()) #방향 회전 정보 입력
    for i in range(l):
        x,c = input().split()
        info.append((int(x),c))

    dx = [0,1,0,-1] #처음에 오른쪽을 보고 있으므로(동 남 서 북)
    dy = [1,0,-1,0]

    def turn(direction,C): #방향을 도는 함수
        if c=='L':
            direction = (direction-1)%4
        else:
            direction = (direction+1)%4
        return direction

    x,y = 1,1 #뱀의 머리 위치
    data[x][y] =2 #뱀이 존재하는 위치를 2로 표시
    direction = 0 #동쪽을 바라보는 걸 표시
    time = 0 #시작한 뒤에 지난 초 시간
    index = 0 #다음 회전 정보 
    q=[(x,y)] #뱀이 차지하고 있는 위치(꼬리가 앞) 
    while True:
        nx = x+dx[direction]
        ny = y+dy[direction]
        if 1<=nx and nx<=N and 1<=ny and ny<=N and data[nx][ny]!=2: #맵 범위 안에 있고 뱀의 몸통이 없는 위치라면
            if data[nx][ny] == 0: #사과가 없다면 이동 후 꼬리 제거
                data[nx][ny] = 2
                q.append((nx,ny))
                px,py = q.pop(0)
                data[px][py] = 0
            if data[nx][ny]==1: #사과가 있다면 이동 후 꼬리 놔두기
                data[nx][ny]=2
                q.append((nx,ny))
        else: #벽이나 뱀의 몸통이 부딪혔다면
            time+=1
            break
        x,y = nx,ny #다음 위치로 머리 이동
        time+=1 #시간 추가
        if index<l and time==info[index][0]: #회전할 시간인 경우 회전
            direction = turn(direction,info[index][1])
            index+=1

    return time

#print(snake())

def build_frame():
    def possible(answer): #현재 설치된 구조물이 가능한 구조물인지 확인하는 함수
        for x,y,stuff in answer: 
            if stuff==0: #설치된게 기둥인 경우
                if y==0 or [x-1,y,1] in answer or [x,y,1] in answer or [x,y-1,0] in answer: #바닥 위 or 보의 한쪽 끝부분 위 or 다른 기둥 위라면 정상
                    continue
                return False #아니라면 return False
            elif stuff==1: #설치된게 보인 경우
                if [x,y-1,0] in answer or [x+1,y-1,0] in answer or ([x-1,y,1] in answer and [x+1,y,1] in answer): #한쪽 끝이 기둥 위 or 양쪽 끝부분이 다른 보와 동시에 연결이면 정상
                    continue
                return False #아니라면 return False
        return True

    def solution(n, build_frame):
        answer = []
        for frame in build_frame:
            x,y,stuff,operate = frame
            if operate == 0: #삭제하는 경우
                answer.remove([x,y,stuff]) #일단 삭제하고
                if not possible(answer): #가능한 구조물인지 확인
                    answer.append([x,y,stuff]) #가능한 구조물이 아니면 다시 설치
            if operate==1: #설치하는 경우
                answer.append([x,y,stuff]) #일단 설치하고
                if not possible(answer): #가능한 구조물인지 확인
                    answer.remove([x,y,stuff]) #가능한 구조물이 아니라면 다시 제거
        return sorted(answer) #정렬된 결과 반환

    return solution(5,[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]])

#print(build_frame)