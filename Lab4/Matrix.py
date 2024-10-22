# Given matrix of size n × m that contains positive integers, not greater than 10000.

# The cells are adjacent if their column or row numbers differ by 1.
# The path from one cell to another passes only through adjacent cells of the matrix.

# Find the path with minimum cost between the upper left and lower right corners of the matrix.
# The cost of the path equals to the sum of matrix elements through the way.
# It is allowed to move to neighboring cells to the left, right, up and down.

# Input
# First line contains the numbers n and m (1 ≤ n, m ≤ 10). Then n lines are given, each line contains m numbers.
# Output
# Print the cost of minimal path.

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
minimal_path = [[1000000] * m for _ in range(n)]
minimal_path[0][0] = matrix[0][0]
queue = [(0, 0)]
while queue:
    x, y = queue.pop(0)
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m:
            new_cost = minimal_path[x][y] + matrix[nx][ny]
            if new_cost < minimal_path[nx][ny]:
                minimal_path[nx][ny] = new_cost
                queue.append((nx, ny))

print(minimal_path[-1][-1])
