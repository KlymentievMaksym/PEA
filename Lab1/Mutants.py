# For a long time in the Institute of Arts, Mutants and Information Technologies, cute colorful animals are bred. 
# For convenience, each color is designated by its own number, there are no more than 10^9 colors in total. 
# One of the beautiful days a miracle happened in the nursery: all the animals were lined up in a row in ascending order of colors. 
# Taking this opportunity, the laboratory assistants decided to count how many animals of different colors live in the nursery, 
# and, according to the law of the genre, they asked you to write a program that will help them in solving this difficult task.

# Input
# The first line contains the number of animals n (0 ≤ n ≤ 10^5) in the Institute. The next line contains n non-decreasing non-negative integers not exceeding 10^9 - their colors. 
# The third line contains the number of requests m (1 ≤ m ≤ 100000) for your program. The next line contains m non-negative integers (not exceeding 10^9 + 1).
# Output
# Print m lines. For each query, print the number of animals of the given color in the nursery.

# Examples
# Input #1
# 10
# 1 1 3 3 5 7 9 18 18 57
# 5
# 57 3 9 1 179
# Answer #1
# 1
# 2
# 1
# 2
# 0

# N = 10
# n = [1, 1, 3, 3, 5, 7, 9, 18, 18, 57]
# M = 5
# m = [57, 3, 9, 1, 179]

N = int(input())
n = list(map(int, input().split()))
M = int(input())
m = list(map(int, input().split()))

count_dict = {}

for color in n:
    count_dict[color] = count_dict.get(color, 0) + 1

for color in m:
    if color in count_dict:
        print(count_dict[color])
    else:
        print(0)
