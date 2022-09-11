from collections import deque
MAX=100001
#문제 : 숨밖꼭질

# N: 현재위치 , K:도달 위치
N,K=map(int,input().split())

graph=[0]*MAX


def bfs(x1,y1):

    queue=deque([x1])

    while queue:
        x=queue.popleft()
        if x==y1:
            return graph[y1]

        dx=[-1,1,x]

        for i in range(3):
            nx=x+dx[i]
            if 0 <= nx < MAX and not graph[nx]:
                graph[nx]=graph[x]+1
                queue.append(nx)
        
    return graph[y1]


queue=deque()
print(bfs(N,K))