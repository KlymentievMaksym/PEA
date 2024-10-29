class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.rank = [1] * (n + 1)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            if self.rank[rootX] >= self.rank[rootY]:
                if self.rank[rootX] == self.rank[rootY]:
                    self.rank[rootX] += 1
                rootX, rootY = rootY, rootX
            self.parent[rootY] = rootX
            return True
        return False


n, m = map(int, input().split())
edges = []

for _ in range(m):
    u, v = map(int, input().split())
    edges.append((u, v))

uf = UnionFind(n)
tree_edges = []

for u, v in edges:
    if uf.union(u, v):
        tree_edges.append((u, v))
        if len(tree_edges) == n - 1:
            break

for u, v in tree_edges:
    print(u, v)
