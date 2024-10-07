# The least common multiple (LCM) of a set of positive integers is the smallest positive integer which is divisible by all the numbers in the set. 
# For example, the LCM of 5, 7 and 15 is 105.

# You need to find the LCM of m given positive integers.

# Input
# The first line contains the number of tests. Each test case is a single line of the form m n[1] n[2] n[3] ... n[m], where m (1 ≤ m ≤ 100) is the number of integers 
# and n[1], ..., n[m] are positive integers. All integers will be positive and lie within the range of a 32-bit integer.
# Output
# For each test case print in a single line the LCM of given m positive integers. All results will lie in the range of a 32-bit integer.

def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


number_of_test_cases = int(input())
for i in range(number_of_test_cases):
    line = list(map(int, input().split()))
    m = line[0]
    numbers = line[1:]
    lcm = numbers[0]
    for num in numbers[1:]:
        lcm = lcm * num // gcd(lcm, num)
    print(lcm)
