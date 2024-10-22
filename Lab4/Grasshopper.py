# One of the teachers has a grasshopper living in their room, and it loves to jump on a one-dimensional checkered board of length n cells.
# Unfortunately for the grasshopper, it can only jump forward by 1,2,…,k cells.

# One day, the teachers became curious about how many ways the grasshopper could jump from the first cell to the last. Help them answer this question.
# Input
# Two integers n and k (1≤n≤30,1≤k≤10).
# Output
# Print the number of ways the grasshopper can jump from the first cell to the last.

n, k = map(int, input().split())

number_of_cells_to_jump_on = [0]*n
if n == 1:
    print(1)
elif n == 2 and k > 1:
    print(2)
else:
    number_of_cells_to_jump_on[0] = 1
    for index_main in range(1, n):
        number_of_cells_to_jump_on[index_main] = sum(number_of_cells_to_jump_on[prev_index] for prev_index in range(max(0, index_main - k), index_main))

    print(number_of_cells_to_jump_on[-1])
