if __name__ == '__main__':
    N = int(input()) #N 입력받기
    arr = [] #arr 초기화
    for i in range(N): #N개만큼 도는 반복문
        string = list(input().split(' ')) #string을 띄어쓰기 단위로 쪼개기
        if string[0]=="insert": #insert인 경우 해당 위치에 삽입
            arr.insert(int(string[1]),int(string[2]))
        if string[0]=="print": #print인 경우 arr print
            print(arr)
        if string[0]=="remove": #remove인 경우 arr에 해당하는 값 remove
            arr.remove(int(string[1]))
        if string[0]=="append": #append인 경우 arr에 추가
            arr.append(int(string[1]))
        if string[0]=="sort": #sort인 경우 정렬
            arr.sort()
        if string[0]=="pop": #pop인 경우 pop
            arr.pop()
        if string[0]=="reverse": #reverse인 경우 reverse
            arr.reverse()