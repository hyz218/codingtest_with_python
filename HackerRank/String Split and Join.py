def split_and_join(line):
    string =  line.split(" ") #split the string by " "
    
    return "-".join(string) #join the string with "-"

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)