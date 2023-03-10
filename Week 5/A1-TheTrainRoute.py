n, m = list(map(int,input().split()))
adj_list = []

def bfs(adj_list, n, u):
    queue = []
    queue.append(u)
    visited = [False] * (n)
    path = [0] * (n)
    visited[u] = True
    while len(queue) > 0:
        u = queue.pop(0)
        for v in adj_list[u]:
            if visited[v]:  continue
            queue.append(v)
            visited[v] = True
            path[v] = path[u] + 1
    return path

def bfs2(adj_list, n, u):
    queue = []
    queue.append(u)
    visited = [False] * (n)
    path = [0] * (n)
    visited[u] = True
    while len(queue) > 0:
        # print(queue)
        u = queue.pop(0)
        for i in range(n):
            if i in adj_list[u]:    
                # print(i)
                continue
            if visited[i]:  
                # print(visited[i])
                continue
            # print(i)
            queue.append(i)
            visited[i] = True
            path[i] = path[u] + 1
    return path


for i in range(n):
    adj_list.append(list())
for i in range(m):
    u, v = list(map(int,input().split()))
    adj_list[u-1].append(v-1)
    adj_list[v-1].append(u-1)
# print(adj_list)
# print(bfs(adj_list,n,1))
# print(bfs2(adj_list,n,0))

m1 = (bfs(adj_list,n,0)[n-1])
m2 = (bfs2(adj_list,n,0)[n-1])

if n-1 in adj_list[0] and m2 != 0:
    print(m2)
elif m1 != 0 and m2 != 0:
    print(m1)
else:
    print("-1")
