# Find such number x that x^2+x^1/2​=C with no less than 6 digits after the decimal point.

# Input
# One real number С (1.0≤C≤10^10).
# Output
# Print the root x with no less than 6 digits after the decimal point.

C = float(input())

smallest = 0
biggest = C
epsilon = 1e-7

while biggest - smallest > epsilon:
    root = (smallest + biggest) / 2
    if root**2 + root**(1/2) < C:
        smallest = root
    else:
        biggest = root

print(f"{root:.6f}")
