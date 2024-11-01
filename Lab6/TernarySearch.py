# Find the minimum of a function f(x)=x2+ax+b.

# Input
# Two integers a and b (∣a∣,∣b∣≤106).
# Output
# Print the value of x where the function f(x) is minimal. Print the answer with 2 decimal digits. It is known that ∣x∣≤100.
def f(x):
    return x**2 + a * x + b


a, b = map(int, input().split())

smallest = -100
biggest = 100
epsilon = 1e-8

while biggest - smallest > epsilon:
    mid1 = (smallest * 2 + biggest) / 3
    mid2 = (smallest + biggest * 2) / 3
    if f(mid1) < f(mid2):
        biggest = mid2
    else:
        smallest = mid1

print(f"{biggest:.2f}")
