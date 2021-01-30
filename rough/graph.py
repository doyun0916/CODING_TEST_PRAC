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
# parent = [0] * (v+1)
#
# for i in range(1, v+1):
#     parent[i] = i
#
# ############################# 서로소 집합 알고리즘 ##################
# for i in range(e):
#     a, b = map(int, input().split())
#     union_parent(parent, a, b)
#
# ############ 싸이클 판별 코드 #############################
# cycle = False
# for i in range(e):
#     a, b = map(int, input().split())
#     if find_parent(parent, a) == find_parent(parent, b):
#         cycle=True
#         break
#     else:
#         union_parent(parent, a, b)
# if cycle:
#     print(cycle)
# else:
#     print(cycle)
#
# ############# 크루스칼 #################################3
# edges = []
# result = 0
# for _ in range(1, v+1):
#     a, b, cost = map(int, input().split())
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
# print(result)

################# Question 1 ################################################
# n개의 여행지. (1~N) 번호
# def find_parent(parent, x):
#     if parent[x] != x:
#         parent[x] = find_parent(parent, parent[x])
#     return parent[x]
#
# def union_parent(parent, a,  b):
#     a = find_parent(parent, a)
#     b = find_parent(parent, b)
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b
#
# n, m = map(int, input().split())
# parent = [0] * (n+1)
#
# for i in range(1, n+1):
#     parent[i] = i
#
# for i in range(1, n+1):
#     a = list(map(int, input().split()))
#     for j in range(len(a)):
#         if a[j] != 0:
#             union_parent(parent, i, j+1)
#
# check = list(map(int, input().split()))
#
# now = parent[check[0]]
# yn = True
# for k in check:
#     if now != parent[k]:
#         yn = False
#         break
#
# if yn:
#     print("Yes")
# else:
#     print("No")

################### Question 2 ###########################################################################
# g = int(input())
# p = int(input())
# port = [0] * (g+1)
# stat = []
# for i in range(p):
#     stat.append(int(input()))
#
# stat.sort()
# c = 0
# check = 0
# for i in range(len(stat)):
#     if stat[i] > i+1:
#         c += 1
#     elif stat[i] == i+1:
#         if check == 1 and stat[i] == stat[i-1]:
#             continue
#         else:
#             check = 1
#             c += 1
#     else:
#         if c == g:
#             break
#         else:
#             continue
#
# print(c)

################# Question 3 ###############################################################
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
# n, m = map(int, input().split())
# parent = [0] * (n+1)
#
# for i in range(1, n+1):
#     parent[i] = i
#
# edges = []
# result = 0
# for _ in range(m):
#     a, b, cost = map(int, input().split())
#     edges.append((cost, a, b))
#
# edges.sort()
# total = 0
# for edge in edges:
#     cost, a, b = edge
#     total += cost
#     if find_parent(parent, a) != find_parent(parent, b):
#         union_parent(parent, a, b)
#         result += cost
#
# print(total - result)

############## Question 4 ##################################################################
# from itertools import combinations
#
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
# parent = [0] * (n+1)
#
# for i in range(1, n+1):
#     parent[i] = i
#
# planet = []
# for i in range(1, n+1):
#     a, b, c = map(int, input().split())
#     planet.append((a, b, c, i))
#
# path = list(combinations(planet, 2))
# paths = []
# for i in range(len(path)):
#     a, b = path[i]
#     x1, y1, z1, num1 = a
#     x2, y2, z2, num2 = b
#     len = min(abs(x1-x2), abs(y1-y2), abs(z1-z2))
#     paths.append((len, num1, num2))
#
# paths.sort()
# result = 0
# for path_single in paths:
#     cost, a, b = path_single
#     if find_parent(parent, a) != find_parent(parent, b):
#         union_parent(parent, a, b)
#         result += cost
#
# print(result)

##################################### Question 5 ####################################################################
##### 위상정렬 #######################################
# from collections import deque
# n, m = map(int, input().split())
# indegree = [0] * (n+1)
# graph = [[] for _ in range(n+1)]
#
# for i in range(m):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     indegree[b] += 1
#
# def topology():
#     result = []
#     q = deque()
#     for i in range(1, n+1):
#         if indegree[i] == 0:
#             q.append(i)
#
#     while q:
#         now = q.popleft()
#         result.append(now)
#         for i in graph[now]:
#             indegree[i] -= 1
#             if indegree[i] == 0:
#                 q.append(i)

####### 답 ############################
from collections import deque

for tc in range(int(input())):
    n = int(input())
    indegree = [0] * (n+1)
    graph = [[False] * (n+1) for i in range(n+1)]
    data = list(map(int, input().split()))
    for i in range(n):
        for j in range(i+1, n):
            graph[data[i]][data[j]] = True
            indegree[data[j]] += 1

    m = int(input())
    for i in range(m):
        a, b = map(int, input().split())
        if graph[a][b]:
            graph[a][b] = False
            graph[b][a] = True
            indegree[a] += 1
            indegree[b] -= 1
        else:
            graph[a][b] = True
            graph[b][a] = False
            indegree[a] -= 1
            indegree[b] += 1

    result = []
    q = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    certain = True
    cycle = False

    for i in range(n):
        if len(q) == 0:
            cycle = True
            break

        if len(q) >= 2:
            certain = False
            break
        
        now = q.popleft()
        result.append(now)
        for j in range(1, n+1):
            if graph[now][j]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    q.append(j)


