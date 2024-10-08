n = int(input())
numbers = list(map(int, input().split()))


def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


lcm = numbers[0]
for num in numbers[1:]:
    lcm = lcm * num // gcd(lcm, num)
print(lcm)
