#순차 탐색 코드
def sequential_search_function(): 
    
    def sequential_search(n, target, array): #순차 탐색 함수
        for i in range(n):
            if array[i]==target: #array에서 target과 일치하는 부분의 index반환
                return i+1
    
    input_data = input().split() #input data 분리
    n= int(input_data[0])
    target = input_data[1]

    array = input().split() #array에 문자 split하여 넣기

    return sequential_search(n,target,array) #순차 탐색 함수에 대입

print(sequential_search_function())

#재귀적으로 구현한 이진 탐색
def recursive_binary_search_function():
    def recursive_binary_search(array,target,start,end):
        if start>end: #start가 end보다 크면 None return
            return None
        mid = (start+end)//2 #mid는 중간값 설정
        if array[mid] == target: #mid가 target에 일치하면 mid return
            return mid
        elif array[mid]>target: #찾는 값이 mid보다 왼쪽에 있다면
            return recursive_binary_search(array,target,start,mid-1) #왼쪽 부분 search
        else: #찾는 값이 mid보다 오른쪽에 있다면
            return recursive_binary_search(array,target,mid+1,end) #오른쪽 부분 search

    n,target = list(map(int,input().split())) #n, target input받기
    array = list(map(int,input().split())) #array input 받기

    result = recursive_binary_search(array, target, 0, n-1) #재귀함수 실행
    if result == None: #결과가 없다면 False return
        return False
    return result+1 #결과가 있다면 return result+1

print(recursive_binary_search_function())

#반복문으로 구현한 이진 탐색
def loop_binary_search_function():
    def loop_binary_search(array, target, start, end):
        while start<=end: #start가 end보다 작을 경우에만 반복문 실행
            mid = (start+end)//2 #mid 설정
            if array[mid] == target: #mid의 값이 target과 같으면 return
                return mid
            elif array[mid]>target: #mid에 해당하는 값이 target보다 크면, 왼쪽 탐색(end를 mid-1로 업데이트)
                end=mid-1
            else: #mid에 해당하는 값이 target보다 작으면, 오른쪽 탐색(start를 mid+1로 업데이트)
                start = mid+1
        return None #해당하는 숫자가 없는 경우 None return

    n,target = list(map(int,input().split())) #n, target input받기
    array = list(map(int,input().split())) #array input 받기

    result = loop_binary_search(array,target,0,n-1) #반복문 이진 탐색 함수 실행
    if result==None: #해당 숫자가 없는 경우 False return
        return False
    else: #결과가 있다면 result+1 return
        return result+1

print(loop_binary_search_function())

import sys
def input_readline(): #문장 인식 방식
    input_data = sys.stdin.readline().rstrip() #map, split보다 빠르다.
    print(input_data)


#부품찾기
def find_component_binary_search():

    def loop_binary_search(array, target, start, end):
            while start<=end: #start가 end보다 작을 경우에만 반복문 실행
                mid = (start+end)//2 #mid 설정
                if array[mid] == target: #mid의 값이 target과 같으면 return
                    return mid
                elif array[mid]>target: #mid에 해당하는 값이 target보다 크면, 왼쪽 탐색(end를 mid-1로 업데이트)
                    end=mid-1
                else: #mid에 해당하는 값이 target보다 작으면, 오른쪽 탐색(start를 mid+1로 업데이트)
                    start = mid+1
            return None #해당하는 숫자가 없는 경우 None return


    N = int(input()) #N 입력받기
    component = list(map(int,input().split())) #부품 받기
    component.sort() #정렬 (이진탐색은 정렬이 되어 있는 상태에서 사용 가능)

    M = int(input()) #M 입력받기
    order = list(map(int,input().split())) #주문 받기

    for i in order: #주문에 있는 부품이 있는지 확인
        result = loop_binary_search(component,i,0,N-1)
        if result != None: #있다면 Yes 반환
            print('Yes',end=' ')
        else: #없다면 No 반환
            print('No',end=' ')

    return result

#계수정렬을 활용한 부품 찾기
def find_component_count_sort():

    N = int(input()) #N 입력받기
    component = [0]*1000001 #component를 모두 0으로 초기화
    for i in input().split(): #input을 받아 있는 부품의 경우 1로 변환
        component[int(i)] = 1

    M = int(input()) #M 입력받기
    order = list(map(int,input().split())) #주문 받기

    for i in order: #주문에 있는 부품을 도는 반복문
        if component[i]==1: #해당 부품이 존재한다면
            print("Yes", end = ' ')
        else: #해당 부품이 존재하지 않는다면
            print("No",end=' ')
    
    return order

#집합 자료형을 활용한 부품 찾기
def find_component_set():
    N = int(input()) #N 입력받기
    component = set(map(int,input().split())) #부품 받아 집합으로 저장

    M = int(input()) #M 입력받기
    order = list(map(int,input().split())) #주문 받기

    for i in order: #주문에 있는 부품을 도는 반복문
        if i in component: #해당 부품이 component set 안에 존재한다면
            print("Yes", end = ' ')
        else: #해당 부품이 존재하지 않는다면
            print("No",end=' ')

    return order