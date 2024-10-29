N = int(input())
grid = [list(input().strip()) for _ in range(N)]

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

start = None
end = None
for i in range(N):
    for j in range(N):
        if grid[i][j] == '@':
            start = (i, j)
        elif grid[i][j] == 'X':
            end = (i, j)

if not start or not end:
    print("N")

queue = [start]
visited = [[False] * N for _ in range(N)]
parent = [[None] * N for _ in range(N)]

visited[start[0]][start[1]] = True

yes = False

while queue:
    x, y = queue.pop(0)

    if (x, y) == end:
        path = end
        while path and path != start:
            px, py = path
            grid[px][py] = '+'
            path = parent[px][py]

        print("Y")
        for line in grid:
            print("".join(line))
        yes = True
        break

    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and grid[nx][ny] in {'.', 'X'}:
            visited[nx][ny] = True
            parent[nx][ny] = (x, y)
            queue.append((nx, ny))
if not yes:
    print("N")
