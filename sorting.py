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