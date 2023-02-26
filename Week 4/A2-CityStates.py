def find(parent, u):
    if u == parent[u]:
        return parent[u]
    # parent[u] = find(parent, parent[u])
    return find(parent, parent[u])

def union(parent, u, v, count):
    u = find(parent, u)
    v = find(parent, v)
    if u < v:
        parent[v] = u
        count -= 1
    elif u > v:
        parent[u] = v
        count -= 1
    return count

t = int(input())

for _ in range(t):
    n, m = list(map(int, input().split()))
    parrent = [i for i in range(n + 1)]
    count = n
    for i in range(m):
        u, v = list(map(int, input().split()))
        count = union(parrent, u, v, count)
    # print(parrent)
    print(count)

    