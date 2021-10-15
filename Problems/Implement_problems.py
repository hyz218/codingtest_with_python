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

print(Lock_and_key())