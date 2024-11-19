# Given a directed weighted graph.
# Find a pair of vertices, the shortest distance from one of them to another is maximum among all pairs of vertices.

# Input
# The first line contains the number of vertices n (1≤n≤100).
# The next n lines of n numbers describe the weighted matrix.
# Here −1 means no edges between vertices, and any non-negative number — the presence of an edge of given weight.
# All elements on the main diagonal are always zero.
# Output
# Print the desired maximum shortest distance.

def floyd(n, graph_matrix):
    dist = graph_matrix.copy()
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(
                    dist[i][j],
                    dist[i][k] + dist[k][j]
                )
    return dist


n = int(input())

graph_matrix = []

for _ in range(n):
    line = list(map(int, input().split()))
    while -1 in line:
        line[line.index(-1)] = float("inf")
    graph_matrix.append(line)

# print(graph_matrix)
# print(floyd(n, graph_matrix))
dist = floyd(n, graph_matrix)
mx = float("-inf")
for line in dist:
    while float("inf") in line:
        line[line.index(float("inf"))] = -1
    mx = max(mx, max(line))
print(mx)
