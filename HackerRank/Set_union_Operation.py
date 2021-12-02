n = int(input())
nlist = list(map(int,input().split()))

m = int(input())
mlist = list(map(int,input().split()))

s = nlist + mlist

print(len(list(set(s))))