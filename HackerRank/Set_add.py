N = int(input())

array = []
for i in range(N):
    array.append(input())

print(len(list(set(array))))