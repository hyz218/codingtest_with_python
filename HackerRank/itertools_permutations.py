from itertools import permutations

S,k = input().split(' ') #split the input data
per = list(permutations(S,int(k))) #using permutation function
per.sort() #sorting the permutation

for i in range(len(per)):
    s = ''
    for j in range(len(per[i])):
        s+=per[i][j] #merge the string
    print(s)