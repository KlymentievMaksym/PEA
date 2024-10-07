# The GCD of two positive integers is the largest integer that divides both the integers without any remainder. 
# The LCM of two positive integers is the smallest positive integer that is divisible by both the integers. 
# A positive integer can be the GCD of many pairs of numbers. Similarly, it can be the LCM of many pairs of numbers. 
# In this problem, you will be given two positive integers. 
# You have to output a pair of numbers whose GCD is the first number and LCM is the second number.

# Input
# The first line contains the number of tests T (T ≤ 100). Each of the next T lines contains two positive integer G and L. Both G and L are less than 2^31.
# Output
# For each test case print in a separate line two positive integers a and b (a ≤ b), which GCD is G and LCM is L. 
# If the answer is not unique, output the pair for which a is minimal. If there is no such pair, print -1.

T = int(input())
for i in range(T):
    G, L = map(int, input().split())
    if G % L != 0:
        print(-1)
    else:
        a, b = G, L
        print(a, b)
