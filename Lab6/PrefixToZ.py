# Автор справді хотів придумати легенду до цієї задачі, але колоквіум з матаналізу хотів автора більше.
# Вам задана коректна префікс-функція деякого рядка. Обчисліть z-функцію цього ж рядка.

# ####Вхідні данні:
# Перший рядок вхідного стандартного потоку містить число N (1 ≤ N ≤ 10^6). Наступний рядок містить N цілих невід'ємних чисел - опис префікс-функції.
# ####Вихідні данні:
# Виведіть єдиний рядок з N цілих невід'ємних чисел - опис z-функції.

n = int(input())
# a = list(map(int, input().split()))
a = input().split()
z = [0] * n


def z_func(s):
    z = [0] * len(s)
    left, right = 0, 0
    for i in range(0, len(s)):
        z[i] = max(0, min(z[i - left], right - i))
        while i + z[i] < len(s) and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] > right:
            left, right = i, i + z[i]
    return z


def prefix(s):
    p = [0] * len(s)
    for i in range(1, len(s)):
        k = p[i - 1]
        while k > 0 and s[k] != s[i]:
            k = p[k - 1]
        if s[k] == s[i]:
            k += 1
        p[i] = k
    return p


z = z_func(a)
p = prefix(a)
print(*z)
print(*p)
