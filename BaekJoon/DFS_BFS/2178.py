from collections import deque

N,M=map(int,input().split())

graph=[]

for _ in range(N):
    graph.append(list(map(int,input())))

#너비 우선 탐색
def bfs(x,y):

    #이동할 네 가지 방향 (상 , 하 , 좌, 우)
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]

    queue=deque()
    queue.append((x,y))

    while queue:
        x,y=queue.popleft()

        #현재 위치에서 4가지 방향으로 위치 확인
        for i in range(4):
            nx= x+dx[i]
            ny= y+dy[i]

            #위치가 벗어났는지 체크
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            
            # 0은 벽이므로 벽쪽으로는 갈 수 없음
            if graph[nx][ny]==0:
                continue

            if graph[nx][ny]==1:  #1 초과일 시, 방문했음을 의미 -> 방문했으니까 방문할 필요 없으니 생략하기 위함
                graph[nx][ny]=graph[x][y]+1 #해당 노드까지 오기까지 횟수
                queue.append((nx,ny))
    return graph[N-1][M-1]


print(bfs(0,0))