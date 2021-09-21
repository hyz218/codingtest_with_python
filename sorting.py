#선택정렬
def selection_sort():
    array = [7,5,9,0,3,1,6,2,4,8]
    
    for i in range(len(array)):
        min_index = i
        for j in range(i+1,len(array)):
            if array[min_index]>array[j]:
                min_index = j
        array[i], array[min_index] = array[min_index],array[i]

    return array

#삽입정렬
def insertion_sort():
    array = [7,5,9,0,3,1,6,2,4,8]
    
    for i in range(1,len(array)):
        for j in range(i,0,-1):
            if array[j]<array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
            else:
                break

    return array

#swap 함수
def swap():
    array = [3,6,7]
    array[0], array[2] = array[2], array[0]

    return array

def quick_sort_fuction():
    array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

    def quick_sort(array, start, end):
        if start>=end: #원소가 한개인 경우 종료
            return
        pivot = start #pivot에 첫번째 원소 지정
        left = start+1 
        right = end
        while left<=right:
            while left<=end and array[left]<=array[pivot]: #pivot보다 큰 데이터를 찾을 때까지 반복
                left+=1
            while right>start and array[right]>=array[pivot]: #pivot보다 작은 데이터를 찾을 때까지 바놉ㄱ
                right-=1
            if left>right: #엇갈렸을 때, 작은 데이터와 pivot swap
                array[right], array[pivot] = array[pivot], array[right]
            else: #엇갈리지 않았다면, 작은 데이터와 큰 데이터 swap
                array[left], array[right] = array[right],array[left]

        #분할 후 왼쪽 부분과 오른쪽 부분에서 각각 정렬
        quick_sort(array,start,right-1) 
        quick_sort(array,right+1,end) 

    quick_sort(array,0,len(array)-1)
    return array


#python의 장점을 살린 quick sort
def quick_sort_function_2():
    array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

    def quick_sort(array):
        if len(array)<=1: #리스트의 원소가 하나라면 종료
            return array

        pivot = array[0] #pivot은 첫번째 원소
        tail = array[1:] #pivot을 제외한 list

        left_side = [x for x in tail if x<=pivot] #분할된 왼쪽 부분
        right_side = [x for x in tail if x>pivot] #분할된 오른쪽 부분

        return quick_sort(left_side) + [pivot] + quick_sort(right_side)

    return quick_sort(array)


#계수정렬
def count_sort():
    #모든 원소의 값은 0보다 크거나 같다고 가정
    array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
    #모든 범위를 포함하는 list, 0으로 값 초기화
    count = [0] * (max(array)+1)

    for i in range(len(array)):
        count[array[i]]+=1 #각 데이터에 해당하는 index 값 증가

    for i in range(len(count)): #list의 정렬 정보 확인
        for j in range(count[i]):
            print(i, end = ' ')

    return count

def sort_function():
    array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

    result = sorted(array) #sorted 함수 활용
    print(result)

    array.sort() #sort 함수 활용
    print(array)

    array2 = [('바나나',2),('사과',5),('당근',3)]
    def setting(data):
        return data[1] #tuple의 두번째 값 기준으로 sort

    result2 = sorted(array,key=setting)
    print(result)

    return result, array,  result2

def top_to_bottom():
    n = input()

    array = []
    for i in range(n):
        array.append(int(input()))

    array.sort(reverse=True) #내림차순 정렬

    return array


def student_score():
    n = int(input())

    array = []
    for i in range(n):
        input_data = input().split()
        array.append((input_data[0],int(input_data[1])))

    array.sort(key=lambda x:x[1]) #두번째 원소로 정렬

    return array

def swap_two_array_k():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))

    a.sort() #오름차순 정렬
    b.sort(reverse=True) #내림차순 정렬

    for i in range(k): #k까지 도는 반복문
        if a[i] < b[i]: #a의 제일 작은 원소가 b의 제일 큰 원소보다 작을 경우
            a[i], b[i] = b[i], a[i] #swap
        else: #아닌 경우 반복문 빠져나오기
            break

    return (sum(a))