# There are n stones, numbered from 1 to n.
# For each i (1≤i≤n), the height of the i-th stone is hi​.
# The frog initially sits on stone 1.
# It repeats the following action several times to reach stone n: if the frog is on stone i, it can jump either to stone i+1 or to stone i+2.
# The cost of moving from the i-th to the j-th stone is ∣hi​−hj​∣.

# Find the minimum cost of moving the frog to stone n.

# Input
# The first line contains the number of stones n (2≤n≤105). The second line contains integers h1​,h2​,...,hn​ (1≤hi​≤104).
# Output
# Print the minimum cost of moving the frog to stone n.

number_of_stones = int(input())
integers = list(map(int, input().split()))
if number_of_stones == 1:
    print(abs(integers[0]-integers[0]))
elif number_of_stones == 2:
    print(abs(integers[1]-integers[0]))
else:
    cost_of_jumps = [0]*number_of_stones
    cost_of_jumps[0] = 0
    cost_of_jumps[1] = abs(integers[1]-integers[0])
    for integer_index in range(2, number_of_stones):
        cost_of_jumps[integer_index] = min(
            cost_of_jumps[integer_index-1] + abs(integers[integer_index-1]-integers[integer_index]),
            cost_of_jumps[integer_index-2] + abs(integers[integer_index-2]-integers[integer_index])
            )  # short jump, long jump

    print(cost_of_jumps[integer_index])

