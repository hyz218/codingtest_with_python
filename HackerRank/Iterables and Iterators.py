from itertools import combinations

N = int(input())
S = list(input().split(' '))
K = int(input())
cnt = 0
combi = list(combinations(S,K))

for i in range(len(combi)):
    if 'a' in combi[i]:
        cnt+=1
print("{0:.3}".format(cnt/len(combi)))