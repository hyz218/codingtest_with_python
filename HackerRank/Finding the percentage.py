if __name__ == '__main__':
    n = int(input())
    student_marks = {} #make the dictionary
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    score = student_marks[query_name] #query_name과 dictionary의 이름이 같은 경우의 score 추출
    
    print("{:.2f}".format(sum(score)/len(score))) #2 decimal places로 표현