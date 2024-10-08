a, b = map(int, input().split())
numbers = list(True for i in range(b + 1))
numbers[1] = False
p = 2
while (p * p <= b):

    if (numbers[p] is True):

        for i in range(p * p, b+1, p):
            numbers[i] = False
    p += 1

count_p = sum(numbers[a:b+1])

if count_p == 0:
    print("Absent")
else:
    for p in range(a, b+1):
        if numbers[p]:
            print(p)
