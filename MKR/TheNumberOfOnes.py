# In arithmetic expression you are allowed to use the number **1**, operations of addition, multiplication and parenthesis. 
# What is the minimum number of ones you need to obtain the positive integer **n**?
# #### Input One integer n (1≤n≤5000).
# #### Output The required number of ones.

n = int(input())
ones_needed = [5001] * (n + 1)
ones_needed[0] = 0
ones_needed[1] = 1

for i in range(2, n + 1):
    ones_needed[i] = min(ones_needed[i], ones_needed[1] + ones_needed[i - 1])

    for j in range(1, int(i**(1/2)) + 1):
        if i % j == 0:
            ones_needed[i] = min(ones_needed[i], ones_needed[j] + ones_needed[i // j])

print(ones_needed[n])
