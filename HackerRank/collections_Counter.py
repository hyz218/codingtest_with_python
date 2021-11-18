from collections import Counter

X = int(input())
mylist = list(map(int,input().split(' ')))
amount = 0

N = int(input())
for i in range(N):
    shoe_size, shoe_price = map(int,input().split(' '))
    if shoe_size in Counter(mylist).keys():
        amount+=shoe_price
        mylist.remove(shoe_size)
    
print(amount)