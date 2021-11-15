from itertools import combinations_with_replacement

S,k = input().split(' ')
combi = list(combinations_with_replacement(S,int(k)))
answer = []
for i in range(len(combi)):
    ans = []
    for j in range(len(combi[i])):
        ans.append(combi[i][j])
    ans.sort()
    answer.append(ans)

answer.sort()
for i in range(len(answer)):
    s=''
    for j in range(len(answer[i])):
        s+=answer[i][j]
    print(s)