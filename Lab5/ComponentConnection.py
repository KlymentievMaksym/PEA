# class UnionFindTable:
#     def __init__(self, sets=[]):
#         while [] in sets:
#             sets.remove([])

#         len_of_sets = len(sets)
#         size_of_sets = 0

#         for set in sets:
#             # size_of_sets += len(set)
#             size_of_sets = max(size_of_sets, max(set))

#         self.r = [0] * size_of_sets
#         self.list = [0] * len_of_sets
#         self.next = [0] * size_of_sets
#         self.size = [0] * len_of_sets
#         self.internal_names = {internal_name+1: len_of_sets-1-internal_name for internal_name in range(len_of_sets)}
#         self.external_names = {external_name: len_of_sets-external_name for external_name in range(len_of_sets-1, -1, -1)}
#         for single_set in sets:
#             index = self.internal_names[sets.index(single_set)+1]
#             for item in single_set:
#                 self.r[item-1] = index
#                 next_item = single_set.index(item)+1
#                 if next_item < len(single_set):
#                     self.next[item-1] = single_set[next_item]
#                 self.size[index] = len(single_set)
#             self.list[index] = single_set[0]

#     def make_sets(self):
#         values_used = []
#         sets = []
#         for key, value in self.internal_names.items():
#             single_set = []
#             if value not in values_used:
#                 values_used.append(value)
#                 number = self.list[value]
#                 k = 0
#                 while number != 0:
#                     # print(number, k)
#                     if number == self.next[self.list[value]-1]:
#                         k += 1
#                         if k >= 2:
#                             print('Break because loop is happening...')
#                             break
#                     single_set.append(number)
#                     number = self.next[number-1]
#                 # print(number, k)
#             sets.append(single_set)
#         return sets

#     def find(self, x):
#         return self.external_names[self.r[x-1]]

#     def union(self, x, y):
#         A = self.internal_names[x]
#         B = self.internal_names[y]
#         if A == B:
#             return self
#         if self.size[A] > self.size[B]:
#             A, B = B, A
#             x, y = y, x
#         z = self.list[A]
#         for _ in range(self.size[A]):
#             self.r[z-1] = B
#             last = z
#             z = self.next[z-1]
#         self.next[last-1] = self.list[B]
#         self.list[B] = self.list[A]
#         self.size[B] += self.size[A]
#         self.internal_names[x] = B
#         self.external_names[B] = x

#         return self

#     def print(self):  # pragma: no cover
#         print('Internal names:', self.internal_names)
#         print('External names:', self.external_names)
#         print('List of r:', self.r)
#         print('List of next:', self.next)
#         print('List of first elements:', self.list)
#         print('Sizes:', self.size)
#         print('Current sets:', self.make_sets())
#         return self


# n, m = map(int, input().split())
# uf = UnionFindTable([[i+1] for i in range(n)])
# for _ in range(m):
#     x, y = map(int, input().split())
#     uf.union(x, y)
# lst = uf.make_sets()
# while [] in lst:
#     lst.remove([])
# print(len(lst))
# for single_set in lst:
#     print(len(single_set))
#     print(*single_set)


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.rank = [1] * (n + 1)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            if self.rank[rootX] >= self.rank[rootY]:
                if self.rank[rootX] == self.rank[rootY]:
                    self.rank[rootX] += 1
                rootX, rootY = rootY, rootX
            self.parent[rootY] = rootX


n, m = map(int, input().split())

uf = UnionFind(n)

for _ in range(m):
    u, v = map(int, input().split())
    uf.union(u, v)

components = {}
for i in range(1, n + 1):
    root = uf.find(i)
    if root not in components:
        components[root] = []
    components[root].append(i)

print(len(components))

for component in components.values():
    print(len(component))
    print(*component)
