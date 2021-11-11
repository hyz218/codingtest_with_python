if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    arr_2 = sorted(list(set(arr)),reverse = True) #sorting the unique list number
    
    print(arr_2[1])
    