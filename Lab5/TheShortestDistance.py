# The directed graph is given. Find the shortest distance from the vertex x to other vertices of the graph.

# Input
# The first line contains two integers n and x (1≤n≤1000,1≤x≤n) — the number of vertices in a graph and the starting vertex.
# Each of the next n lines contains n numbers — the adjacency matrix of the graph:
# the i-th line and j-th column contains "1", if the vertices i and j are connected with the edge, and "0",
# if there is no edge between them. The main diagonal contains zeroes.

# Output
# Print the numbers d1​,d2​,...,dn​, where di​ is −1 if there is no path from x to i, or the minimal distance from x to i otherwise.

n, x = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
dist = [-1] * n
dist[x - 1] = 0
queue = [(x - 1, 0)]
while queue:
    u, d = queue.pop(0)
    for v in range(n):
        if matrix[u][v] == 1 and dist[v] == -1:
            dist[v] = d + 1
            queue.append((v, d + 1))
print(*dist)
