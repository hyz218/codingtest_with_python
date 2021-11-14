from itertools import combinations

S,k = input().split() #split the input data
for i in range(1,int(k)+1):
    answer=[]
    combi = list(combinations(S,i)) #using combination function
    for j in range(len(combi)):
        com = []
        for k in range(len(combi[j])):
            com.append(combi[j][k]) #append the combination functions output
        com.sort() #sorting the string
        answer.append(com)

    ans = []
    for j in range(len(answer)): #making the list to string
        s=''
        for k in range(len(answer[j])):
            s+=answer[j][k]
        ans.append(s)
     
    ans.sort()
    for j in ans: #print the result
        print(j)