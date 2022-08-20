from collections import deque
import sys

queue=deque()

for i in range(int(input())):
    data=list(sys.stdin.readline().rstrip().split())
    what=data[0]
    if what=='push':
        queue.append(data[1])
    if what=='pop':
        if queue:
            print(queue.popleft())
        else:
            print("-1")
    if what=='size':
            print(len(queue))
    if what=='empty':
        if queue:
            print("0")
        else:
            print("1")
    if what=="front":
        if queue:
            print(queue[0])
        else:
            print("-1")
    if what=="back":
        if queue:
            print(queue[-1])
        else:
            print("-1")



    