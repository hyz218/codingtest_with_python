from collections import deque

d = deque()

N = int(input())
for i in range(N):
    s = input().split(' ')
    if s[0]=='append':
        d.append(int(s[1]))
    if s[0]=='appendleft':
        d.appendleft(int(s[1]))
    if s[0]=='pop':
        d.pop()
    if s[0]=='popleft':
        d.popleft()

for i in range(len(d)):
    print(d[i],end=' ')