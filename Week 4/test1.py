import collections
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, u):
        if u != self.parent[u]:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    
    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu != pv:
            if self.rank[pu] < self.rank[pv]:
                pu, pv = pv, pu
            self.parent[pv] = pu
            if self.rank[pu] == self.rank[pv]:
                self.rank[pu] += 1
    
    def groups(self):
        groups = collections.defaultdict(list)
        for i in range(len(self.parent)):
            groups[self.find(i)].append(i)
        return groups

def count_permutations(n, a, b, x):
    dsu = DSU(n)
    for i in range(n):
        if x[i]:
            if x[i] == a[i]:
                dsu.union(i, a.index(x[i]))
            else:
                dsu.union(i, b.index(x[i]))
    
    for i in range(n):
        if not x[i]:
            for j in range(n):
                if i != j and (a[i] == a[j] or a[i] == b[j] or b[i] == a[j] or b[i] == b[j]):
                    dsu.union(i, j)
                    
    groups = dsu.groups()
    ans = 1
    mod = 1000000007
    for group in groups.values():
        count = 0
        for i in group:
            if x[i]:
                if (x[i] != a[i] and x[i] != b[i]):
                    count = -1
                    break
            else:
                count += 1
        if count == -1:
            continue
        if count == 0:
            count = 1
        ans = (ans * count) % mod
    return ans

# Sample input
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    x = list(map(int, input().split()))
    print(count_permutations(n, a, b, x))
