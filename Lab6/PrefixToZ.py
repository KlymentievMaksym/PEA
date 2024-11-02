# Автор справді хотів придумати легенду до цієї задачі, але колоквіум з матаналізу хотів автора більше.
# Вам задана коректна префікс-функція деякого рядка. Обчисліть z-функцію цього ж рядка.

# ####Вхідні данні:
# Перший рядок вхідного стандартного потоку містить число N (1 ≤ N ≤ 10^6). Наступний рядок містить N цілих невід'ємних чисел - опис префікс-функції.
# ####Вихідні данні:
# Виведіть єдиний рядок з N цілих невід'ємних чисел - опис z-функції.

# def z_func(s):
#     length = len(s)
#     z = [0] * length
#     for i in range(1, length):
#         while i + z[i] < length and s[z[i]] == s[i + z[i]]:
#             z[i] += 1
#     return z


# def prefix_func(s):
#     length = len(s)
#     p = [0] * length
#     for i in range(length):
#         for k in range(i+1):
#             if s[0:k] == s[i-k+1:i+1]:
#                 p[i] = k
#     return p


# def p_to_z_func(p):
#     length = len(p)
#     z = [0] * length
#     for i in range(1, length):
#         if p[i] > 0:
#             z[i - p[i] + 1] = p[i]
#             for j in range(1, p[i]):
#                 if z[i - p[i] + 1 + j] < p[i] - j:
#                     z[i - p[i] + 1 + j] = p[i] - j
#     return z



# # s = 'abcabcd'
# s = 'aaaaa'

# p = prefix_func(s)
# z_result_p = p_to_z_func(p)

# print(p)
# print(z_func(s))
# print(z_result_p)


def p_to_z_func(p):
    length = len(p)
    z = [0] * length
    for i in range(1, length):
        if p[i] > 0:
            z[i - p[i] + 1] = p[i]
            for j in range(1, p[i]):
                if z[i - p[i] + 1 + j] < p[i] - j:
                    z[i - p[i] + 1 + j] = p[i] - j
    return z

n = int(input())
p = list(map(int, input().split()))
print(*p_to_z_func(p))