import sys
from collections import deque

size=int(sys.stdin.readline())
st=[]
top=0

for i in range(size):
    data=list(sys.stdin.readline())
    print(data)
    for j in data:
        if j==' ' or j=='\n':
            while(len(st)):
                print(st.pop(),end='')
            print(" ",end='')
        else:
            st.append(j)
            top+=1
    # while(len(st)):
    #     print(st.pop(),end='')
    data.clear()

        # print("하나씩: "+j+"\n")
    




#다른 사람 참고
# for i in range(int(sys.stdin.readline())):
#     word=sys.stdin.readline().rstrip()[::-1].split()
#     word.reverse()

#     print(' '.join(word))