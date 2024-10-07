# Given the values of a and b, print all primes in the interval from a to b inclusively.

# Input
# Two integers a and b(1≤a≤b≤105).
# Output
# Print in one line all prime numbers in the interval from a to b inclusively.

a, b = map(int, input().split())
numbers = list(True for i in range(b + 1))
numbers[1] = False
p = 2
while (p * p <= b):

    if (numbers[p] is True):

        for i in range(p * p, b+1, p):
            numbers[i] = False
    p += 1

count = 0
count_p = sum(numbers[a:b+1])

for p in range(a, b+1):
    if numbers[p]:
        count += 1
        if count == count_p:
            print(p)
        else:
            print(p, end=" ")

