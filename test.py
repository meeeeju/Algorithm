from collections import deque
import sys

# input=sys.stdin.readline


p=[(0,0),(0,1),(0,2),(-1,2),(-1,3),(2,4)]

# p=sorted(p,key=lambda x : (x[0],-x[1]))

print(p.sort(key=lambda p: p[0]))
print(p)
