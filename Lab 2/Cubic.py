# Given a cubic equation
# ax3+bx2+cx+d=0(a != 0)
# It is known that this equation has exactly one root. Find it.

# Input
# Four integers: a,b,c,d (−1000≤a,b,c,d≤1000).
# Output
# Print the root of equation with no less than **6** decimal digits.

def f(x, a, b, c, d):
    return a * x**3 + b * x**2 + c * x + d

a, b, c, d = map(int, input().split())

left, right = -2000, 2000
epsilon = 1e-10

while right - left > epsilon:
    mid = (left + right) / 2
    if f(mid, a, b, c, d) == 0:
        root = mid
        break
    elif f(mid, a, b, c, d) * f(left, a, b, c, d) < 0:
        right = mid
    else:
        left = mid

root = (left + right) / 2

print(f"{root:.6f}")