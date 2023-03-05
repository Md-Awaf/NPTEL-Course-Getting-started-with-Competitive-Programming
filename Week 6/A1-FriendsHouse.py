def bfs(adj_list, n, u, end):
    queue = []
    queue.append(u)
    visited = [False] * (n)
    path = [0] * (n)
    visited[u] = True
    while len(queue) > 0:
        u = queue.pop(0)
        if u == end:
            return path
        for v in adj_list[u]:
            if visited[v]:  continue
            queue.append(v)
            visited[v] = True
            path[v] = path[u] + 1
    return path

adj_list = []
n, m, x, y = list(map(int,input().split()))
for i in range(n):
    adj_list.append(list())
for i in range(m):
    u, v = list(map(int,input().split()))
    adj_list[u-1].append(v-1)
    adj_list[v-1].append(u-1)
    
count = 0
m1 = (bfs(adj_list,n,x-1, y-1))
lenght = m1[y-1]
# print(lenght)
for u in range(n):
    for v in range(u+1,n):
        if v not in adj_list[u]:
            adj_list[u].append(v)
            adj_list[v].append(u)
            if (bfs(adj_list,n,x-1, y-1))[y-1] < lenght:
                adj_list[u].pop()
                adj_list[v].pop()
            else:
                # print(u,v)
                count += 1
                adj_list[u].pop()
                adj_list[v].pop()
print(count)