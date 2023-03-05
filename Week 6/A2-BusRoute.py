import heapq as hq
import math, sys

def dijkstra(G, s):
    n = len(G)
    visited = [False]*n
    weights = [math.inf]*n
    path = [None]*n
    queue = []
    weights[s] = 0
    hq.heappush(queue, (0, s))
    while len(queue) > 0:
        g, u = hq.heappop(queue)
        visited[u] = True
        for v, w in G[u]:
            if not visited[v]:
                f = g + w
                if f < weights[v]:
                    weights[v] = f
                    path[v] = u
                    hq.heappush(queue, (f, v))
    return path, weights

n, m = list(map(int,input().split()))
if m == 0:
    print(0)
    sys.exit()
G = [list() for i in range(n+1)]

for i in range(m):
    u, v, w = list(map(int,input().split()))
    # print(u, v, w)
    G[u].append((v,w))
    G[v].append((u,w))

# print(G)
ans = dijkstra(G, 1)[1][n]
print(-1 if ans == math.inf else ans)