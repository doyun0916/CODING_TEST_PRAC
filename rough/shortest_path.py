# 1 ~ N 까지 회사
# 서로 도로로 연결
# A는 1번 회사에 있음 ~ x에 방문해 물건 팜
# 회사 - 회사 : 연결 1
# 소개팅 상대는 k번 회사에
# 존재
# 1 -> k -> x
# 최소 시간은?

import heapq
# import sys
# input = sys.stdin.readline
# INF = int(1e9)
#
# n, r = map(int, input().split())
# gra = [[INF] * (n+1) for i in range(n+1)]
# for a in range(n+1):
#     for b in range(n+1):
#         if a==b:
#             gra[a][b] = 0
# for i in range(r):
#     a, b = map(int, input().split())
#     gra[a][b] = 1
#     gra[b][a] = 1
#
# x, k = map(int, input().split())
#
# for k in range(1, n+1):
#     for a in range(1, n+1):
#         for b in range(1, n+1):
#             gra[a][b] = min(gra[a][b], gra[a][k] + gra[k][b])
#
# distance = gra[1][k] + gra[k][x]
#
# if distance >= INF:
#     print("INFINITY")
# else:
#     print(distance)
#
#
#
# n, m, c = map(int, input().split())
# INF = int(1e9)
# graph = [[] for i in range(n+1)]
# distance = [INF] * (n+1)
# for _ in range(m):
#     x, y, z = map(int, input().split())
#     graph[x].append((y, z))
#
# def dijkstra(start):
#     q = []
#     heapq.heappush(q, (0, start))
#     distance[start] = 0
#     while q:
#         dist, now = heapq.heappop(q)
#         if distance[now] < dist:
#             continue
#         for i in graph[now]:
#             cost = dist + i[1]
#             if cost < distance[i[0]]:
#                 distance[i[0]] = cost
#                 heapq.heappush(q, (cost, i[0]))
#
# dijkstra(c)
#
# count = 0
# max_distance = 0
# for d in distance:
#     if d != INF:
#         count += 1
#         max_distance = max(max_distance, d)
#
# print(count - 1, max_distance)
#
#
# ##################################################### 문제
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
#     n, m = map(int, input().split())
#     parent = [0] * (n+1)
#
#     for i in range(0, n+1):
#         parent[i] = i
#
#     for i in range(m):
#         oper, a, b = map(int, input().split())
#         if oper == 0:
#             union_parent(parent, a, b)
#         elif oper == 1:
#             if find_parent(parent, a) == find_parent(parent, b):
#                 print('YES')
#             else:
#                 print('NO')
#
# ########################################################
#
# def find_parent(parent, x):
#     if parent[x] != x:
#         parent[x] = find_parent(parent, parent[x])
#     else:
#         return parent[x]
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
# edges = []
# result = 0
#
# for i in range(1, v + 1):
#     parent[i] = i
#
# for _ in range(e):
#     a, b, cost = map(int, input().split())
#     edges.append((cost, a, b))
#
# edges.sort()
# last = 0
#
# for edge in edges:
#     cost, a, b = edge
#     if find_parent(parent, a) != find_parent(parent, b):
#         union_parent(parent, a, b)
#         result += cost
#         last = cost
# print(result - last)

###################################################################
import sys
from collections import deque
import copy
input = sys.stdin.readline

v = int(input())
indegree = [0] * (v+1)
graph = [[] for i in range(v+1)]
time = [0] * (v+1)

for i in range(1, v+1):
    data = list(map(int, input().split()))
    time[i] = data[0]
    for x in data[1:-1]:
        indegree[i] += 1
        graph[x].append(i)

def topology_sort():
    result = copy.deepcopy(time)
    q = deque()
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for i in range(1, v+1):
        print(result[i])

topology_sort()