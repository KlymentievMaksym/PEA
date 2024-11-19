# During robbery in a store a thief found n boxes with golden sand.
# All the sand in a box number i has the cost v[i] and the weight w[i].
# To carry the stolen sand, thief uses a knapsack.
# Find the highest total cost of sand that the robber can carry out, if knapsack capacity is limited to w.

# One can pour from the boxes any amount of sand,
# while the ratio of the cost of the poured sand to the cost of the entire box is equal to the ratio of volume of the poured sand to the volume of entire sand box.

# Input
# The first line contains two integers n and w (1 ≤ n ≤ 1000, 1 ≤ w ≤ 10^6).
# Each of the next n lines contains two integers.
# The i-th line contains the price v[i] and weight w[i] of the sand in the i-th box.
# All numbers are non-negative and do not exceed 10^6.
# Output
# Print the desired maximum cost with 3 digits after the decimal point.

def fractional_knapsack(n, w, items):
    items.sort(key=lambda x: x[0] / x[1], reverse=True)

    total_value = 0.0
    for value, weight in items:
        take_weight = min(weight, w)
        total_value += take_weight * (value / weight)
        w -= take_weight

    return total_value


n, w = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(n)]

max_cost = fractional_knapsack(n, w, items)

print(f"{max_cost:.3f}")