n, m = list(map(int,input().split()))
adj_list = []

def bfs(adj_list, n, u):
    queue = []
    queue.append(u)
    visited = [False] * (n + 1)
    path = [0] * (n + 1)
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
    visited = [False] * (n + 1)
    path = [0] * (n + 1)
    visited[u] = True
    count = 0
    while len(queue) > 0 and count<20:
        # print(queue)
        u = queue.pop(0)
        for i in range(1,n+1):
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
            count += 1
    return path


for i in range(n + 1):
    adj_list.append(list())
for i in range(m):
    u, v = list(map(int,input().split()))
    adj_list[u].append(v)
    adj_list[v].append(u)
# print(adj_list)
# print(bfs(adj_list,n,1))
# print(bfs2(adj_list,n,1))

m1 = (bfs(adj_list,n,1)[n])
m2 = (bfs2(adj_list,n,1)[n])
# if m1 == 0 or m2 == 0:
#     print("-1", end="")
# else:
#     print(max(m1, m2), end="")
# print(m1, m2)

if n in adj_list[1] and m2 != 0:
    print(m2)
elif m1 != 0 and m2 != 0:
    print(m1)
else:
    print("-1", end="")
