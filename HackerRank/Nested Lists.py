if __name__ == '__main__':
    # records = []
    # names = []
    # for _ in range(int(input())):
    #     record = []
    #     record.append(input())
    #     record.append(float(input()))
    #     records.append(record)
    
    # records = sorted(records,key = lambda student: student[1])
    # second_lowest_grade = records[1][1]
    
    # for i in range(0,len(records)):
    #     if records[i][1] == second_lowest_grade:
    #         names.append(records[i][0])
            
    # names.sort()
    # for i in names:
    #     print(i)
    
    score_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        score_list.append([name, score])
    second_highest = sorted(set([score for name, score in score_list]))[1]
    print('\n'.join(sorted([name for name, score in score_list if score == second_highest])))