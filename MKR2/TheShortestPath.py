# The undirected graph is given.
# Find the shortest path from vertex a to vertex b.

# Input
# The first line contains two integers n and m (1 ≤ n ≤ 5 * 10^4, 1 ≤ m ≤ 10^5) - the number of vertices and edges.
# The second line contains two integers a and b - the starting and ending point correspondingly.
# Next m lines describe the edges.
# Output
# If the path between a and b does not exist, print -1.
# Otherwise print in the first line the length l of the shortest path between
# these two vertices in number of edges, and in the second line print l + 1 numbers - the vertices of this path.

def shortest_path(n, a, b, edges):
    graph = [[] for _ in range(n + 1)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    dist = [-1] * (n + 1)
    parent = [-1] * (n + 1)
    queue = [a]
    dist[a] = 0

    while queue:
        current = queue.pop(0)
        for neighbor in graph[current]:
            if dist[neighbor] == -1:
                dist[neighbor] = dist[current] + 1
                parent[neighbor] = current
                queue.append(neighbor)
                if neighbor == b:
                    break

    if dist[b] == -1:
        return -1, []
    else:
        path = []
        current = b
        while current != -1:
            path.append(current)
            current = parent[current]
        path.reverse()
        return dist[b], path


n, m = map(int, input().split())
a, b = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]

length, path = shortest_path(n, a, b, edges)

if length == -1:
    print(-1)
else:
    print(length)
    print(' '.join(map(str, path)))
