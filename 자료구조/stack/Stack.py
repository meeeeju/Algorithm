import sys
from collections import deque

size=int(sys.stdin.readline())


st =[]
top=0
for i in range(size):
    data=sys.stdin.readline().rstrip().split()
    if (data[0]=='push'):
        st.append(int(data[1]))
        top+=1
    if (data[0]=='pop'):
        if len(st)== 0:
            print('-1')
        else:
            print(st.pop())
    if (data[0]=='size'):
        print(len(st))
    if (data[0]=='top'):
        if len(st)==0:
            print("-1")
        else:
            top=len(st)-1
            print(st[top])
    if (data[0]=='empty'):
        if len(st)==0:
            print("1")
        else:
            print("0")



