# ## Q 41 ##
# def find_parent(parent, x):
#     if parent[x] != x:
#         parent[x] = find_parent(parent, parent[x])
#     return parent[x]
#
# def union_parent(parent, a, b):
#     a = find_parent(parent, a)
#     b = find_parent(parent, b)
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b
#
# n, m = map(int, input().split())  # 여행지 수, 여행계획 도시수
# parent = [0] * (n+1)
#
# for i in range(1, n+1):
#     parent[i] = i
#
# arr = []
# for i in range(n):
#     arr.append(list(map(int, input().split())))
#
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if arr[i-1][j-1] == 1:
#             union_parent(parent, i, j)
#
# lis = list(map(int, input().split()))
# curr = parent[lis[0]]
# result = True
# for i in range(1, len(lis)):
#     if curr != parent[lis[i]]:
#         result = False
#         break
#
# if result:
#     print("YES")
# else:
#     print("NO")

## Q42 ##
# # def find_parent(parent, x):
# #     if parent[x] != x:
# #         parent[x] = find_parent(parent, parent[x])
# #     return parent[x]
# #
# # def union_parent(parent, a, b):
# #     a = find_parent(parent, a)
# #     b = find_parent(parent, b)
# #     if a < b:
# #         parent[b] = a
# #     else:
# #         parent[a] = b
# v = int(input())
# e = int(input())
# # parent = [0] * (v+1)
# #
# # for i in range(1, v+1):
# #     parent[i] = i
# arr = [0] * (v+1)
# for i in range(e):
#     a = int(input())
#     c = 0
#     temp = True
#     for j in range(a, 0, -1):
#         if arr[a] == 0:
#             arr[a] = 1
#             break
# print(arr.count(1))

# ## Q43 ##
# def find_parent(parent, x):
#     if parent[x] != x:
#         parent[x] = find_parent(parent, parent[x])
#     return parent[x]
#
# def union_parent(parent, a, b):
#     a = find_parent(parent, a)
#     b = find_parent(parent, b)
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b
#
# v, e = map(int, input().split())
# parent = [0] * (v)
# for i in range(v):
#     parent[i] = i
#
# edges = []
# result = 0
# total = 0
# for _ in range(e):
#     a, b, cost = map(int, input().split())
#     total += cost
#     edges.append((cost, a, b))
#
# edges.sort()
#
# for edge in edges:
#     cost, a, b = edge
#     if find_parent(parent, a) != find_parent(parent, b):
#         union_parent(parent, a, b)
#         result += cost
#
# print(total - result)

## Q44 ##
# from itertools import combinations
# def find_parent(parent, x):
#     if parent[x] != x:
#         parent[x] = find_parent(parent, parent[x])
#     return parent[x]
#
# def union_parent(parent, a, b):
#     a = find_parent(parent, a)
#     b = find_parent(parent, b)
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b
#
# n = int(input())
# parent = [0] * n
# for i in range(n):
#     parent[i] = i
#
# q = []
# result = 0
# for i in range(n):
#     x, y, z = map(int, input().split())
#     q.append((x, y, z))
#
# lis = list(combinations(q, 2))
# edges = []
# for list in lis:
#     a, b = list
#     cost = min(abs(a[0]-b[0]), abs(a[1]-b[1]), abs(a[2]-b[2]))
#     edges.append((cost, a, b))
#
# edges.sort()
#
# for edge in edges:
#     cost, a, b = edge
#     a = q.index(a)
#     b = q.index(b)
#     if find_parent(parent, a) != find_parent(parent, b):
#         union_parent(parent, a, b)
#         result += cost
#
# print(result)

## Q45 ##
from collections import deque

def topology_sort():
    result = []
    q = deque()
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    return result

n = int(input())
for _ in range(n):
    v = int(input())
    last_rank = list(map(int, input().split()))
    chan_num = int(input())
    graph = [[] for _ in range(v+1)]
    indegree = [0] * (v+1)

    for a, b in zip(last_rank, last_rank[1:]):
        graph[a].append(b)
        indegree[b] += 1

    for i in range(chan_num):
        a, b = map(int, input().split())
        graph[b].append(a)
        indegree[a] += 1

    res = topology_sort()
    if len(res) != v:
        print("IMPOSSIBLE")
    else:
        print(res)