#Data structure

# 스택 기능
def stack_function():

    stack = []
    stack.append(4)
    stack.append(8)
    stack.append(10)
    stack.pop()
    
    print(stack)
    
    stack.append(1)
    stack.append(2)
    
    print(stack)
    print(stack[::-1])

    return stack

from collections import deque
#큐 기능
def queue_function():

    queue = deque()

    queue.append(5)
    queue.append(1)
    queue.append(4)
    queue.append(8)
    queue.popleft()
    queue.append(7)
    queue.append(6)
    queue.popleft()

    print(queue)
    queue.reverse()
    print(queue)

    return queue


def factorial_iterative(n):
    result = 1
    for i in range(1,n+1):
        result*=i
    return result

def factorial_recursive(n):
    if n<=1:
        return 1
    return n*factorial_recursive(n-1)

if __name__ == "__main__":
    print("Data structure")