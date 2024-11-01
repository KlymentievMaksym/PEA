# There is a rectangular grid of size n rows and m columns. Each cell of the grid contains one integer.
# You can start the route from any cell of the top row.
# Each time you can move to one of the "lower neighbouring" cells 
# (
# in other words, from the cell number (i,j) its possible to go either to (i+1,j−1), or to (i+1,j) or to (i+1,j+1);
# in the case j=m the last of the three options becomes impossible, in the case j=1 the first option becomes impossible
# ).
# And you can finish the route at any cell of the bottom row.

# Write a program that finds the maximum possible sum of the values on the cells traversed among all the possible paths and the number of paths in which this amount is reached.

# Input
# The first line contains numbers n and m (1≤n,m≤200) — the number of rows and columns. Each of the next n lines contains m integers (each number is no more than 106 by absolute value) — the values of the cells in the grid.
# It is known that the required number of paths with maximum sum does not exceed 10^9
# Output
# Print two numbers - the maximum possible sum and the number of paths.

n, m = map(int, input().split())

grid = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    grid[i] = list(map(int, input().split()))

max_pos_sum = [[0] * m for _ in range(n)]
count = [[0] * m for _ in range(n)]

for j in range(m):
    max_pos_sum[0][j] = grid[0][j]
    count[0][j] = 1

for i in range(1, n):
    for j in range(m):
        max_sum = float('-inf')
        ways = 0

        for nj in [j-1, j, j+1]:
                if 0 <= nj < m:
                    if max_pos_sum[i-1][nj] + grid[i][j] > max_sum:
                        max_sum = max_pos_sum[i-1][nj] + grid[i][j]
                        ways = count[i-1][nj]
                    elif max_pos_sum[i-1][nj] + grid[i][j] == max_sum:
                        ways += count[i-1][nj]
        max_pos_sum[i][j] = max_sum
        count[i][j] = ways

last_row = max_pos_sum[n-1]
max_sum = max(last_row)
max_paths = sum(count[n-1][j] for j in range(m) if max_pos_sum[n-1][j] == max_sum)
print(max_sum, max_paths)
