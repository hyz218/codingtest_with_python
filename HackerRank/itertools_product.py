from itertools import product

A = map(int,input().split(' '))
B = map(int,input().split(' '))

prod = list(product(A,B))
for i in range(len(prod)):
    print(prod[i],end=' ')