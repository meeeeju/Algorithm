import sys
import time



left=list(sys.stdin.readline().rstrip()) #apple
right=[]

for j in range(int(sys.stdin.readline())):
    data=list(sys.stdin.readline().rstrip().split())
    what=data[0]
    if what=='L':
        if left:
            right.append(left.pop())
    if what=='D':
        if right:
            left.append(right.pop())
    if what=='B':
        if left:
            left.pop()
    if what=='P':
        left.append(data[1])
print(''.join(left+right[::-1]))


    
        
        

