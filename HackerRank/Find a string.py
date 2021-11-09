def count_substring(string, sub_string):
    cnt = 0 #count of the number
    for i in range(0,len(string)-len(sub_string)+1):
        strings = string[i:len(sub_string)+i] #split the string
        if strings == sub_string:
            cnt+=1
    return cnt

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)