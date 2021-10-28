#from itertools import combinations #memory error
#
#def solution(A):
#    count = 0
#    combi = list(combinations(A, 3))
#
#    for i in range(len(combi)):
#        if (combi[i][0] + combi[i][1] > combi[i][2]) and (combi[i][1] + combi[i][2] > combi[i][0]) and (combi[i][2] + combi[i][0] > combi[i][1]):
#            count+=1
#    return count