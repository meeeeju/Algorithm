#적록색약 2
from collections import deque
import sys

def bfs(x,y,c):   #c: currentcolor 
    visited[x][y]=1
    queue=deque()
    queue.append((x,y))

    while queue:
        x1,y1=queue.popleft()
        for i in range(4):
            nx=x1+mx[i]
            ny=y1+my[i]
            if nx<0 or nx >= N or ny<0 or ny >= N :
                continue
            if not visited[nx][ny] and matrix[nx][ny]==c:
                queue.append((nx,ny))
                visited[nx][ny]=1
                # matrix[nx][ny]='P'
    return



N=int(input())
matrix=[]
visited=[[0]*N for _ in range(N)]
cnt=0
second_cnt=0


mx=[-1,1,0,0]
my=[0,0,-1,1]

for i in range(N):
    matrix.append(list(input()))

for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                if matrix[i][j]=='R':
                    cnt=cnt+1
                    bfs(i,j,'R')
                if matrix[i][j]=='G':
                    cnt=cnt+1
                    bfs(i,j,'G')
                if matrix[i][j]=='B':
                    cnt=cnt+1
                    bfs(i,j,'B')


visited=[[0]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if matrix[i][j] == 'G':
            matrix[i][j] = 'R'

for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                if matrix[i][j]=='R':
                    second_cnt=second_cnt+1
                    bfs(i,j,'R')
                if matrix[i][j]=='B':
                    second_cnt=second_cnt+1
                    bfs(i,j,'B')



print(cnt,second_cnt)




