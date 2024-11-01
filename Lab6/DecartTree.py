import math


def binomial_coeff(n, k):
    if k > n:
        return 0
    return math.comb(n, k)


def calculate_sizes(sizes, v):
    if v == 0:
        return 0
    left, right = tree[v]
    sizes[v] = 1 + calculate_sizes(sizes, left) + calculate_sizes(sizes, right)
    return sizes[v]


def count_ways(tree, sizes, v):
    if v == 0:
        return 1
    left, right = tree[v]
    left_ways = count_ways(tree, sizes, left)
    right_ways = count_ways(tree, sizes, right)
    left_size = sizes[left]
    right_size = sizes[right]
    return left_ways * right_ways * binomial_coeff(left_size + right_size, left_size)


n = int(input())
tree = [None] * (n + 1)
sizes = [0] * (n + 1)

for i in range(1, n + 1):
    left, right = map(int, input().split())
    tree[i] = (left, right)


calculate_sizes(sizes, 1)
print(count_ways(tree, sizes, 1))