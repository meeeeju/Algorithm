from collections import deque
import sys
people_num,count=map(int,sys.stdin.readline().rstrip().split())
answer=list([0]*people_num)
queue=deque([0]*(people_num))

for i in range(people_num): 
    queue[i]=i+1

for j in range(people_num):
    for i in range(1,count+1):
        if (i==count):
            answer[j]=queue.popleft()
        else:
            queue.append(queue.popleft())
        
print('<' + ', '.join(map(str,answer)) + '>')


