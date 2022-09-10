from collections import deque
# n(정점) m(간선) v(간선)


#Depth First Search
def DFS(graph, root):
    visited=[]
    stack=[root]
    while stack :
        n= stack.pop()
        if n not in visited:
            visited.append(n)
            if n in graph :
                temp=list(graph[n]-set(visited))
                temp.sort(reverse=True)
                stack += temp
    return " ".join(str(i) for i in visited)


#Breadth First Search
def BFS(graph, root):
    visited=[]
    queue=deque([root])
    while queue:
        n=queue.popleft()
        if n not in visited:
            visited.append(n)
            if n in graph:
                temp=list(graph[n]-set(visited))
                temp.sort()
                queue+=temp
    return " ".join(str(i) for i in visited)



#그래프 만들기
n , m, start= map(int,input().split())
graph=dict.fromkeys(range(1,n+1))
value=[[] for i in range(n)]
for i in range(m):
    a,b=map(int,input().split())
    value[a-1].append(b)
    value[b-1].append(a)
for i in range(n):
    graph[i+1]=set(value[i])


print(DFS(graph,start))
print(BFS(graph,start))


