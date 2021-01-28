# #################### 다익스트라 ###########
# 1. 그래프, distance 만든다. 2. graph 채운다.  3. heapq push, while pop  4. print
# import heapq
# import sys
# input = sys.stdin.readline
# INF = int(1e9)
# n, m = map(int, input().split())
# start = int(input())
# graph = [[] for i in range(n+1)]
# distance = [INF] * (n+1)
#
# for _ in range(m):
#     a, b, c = map(int, input().split())
#     graph[a].append((b, c))
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
# dijkstra(start)
#
# for i in range(1, n+1):
#     if distance[i] == INF:
#         print("INFINITY")
#     else:
#         print(distance[i])

############# 플로이드 워셜 ###########################
# 1. 2차원 graph 만든다. 2. 자기자신 0으로 3. 그래프 채운다. 4. min 넣는다. 5. print
#
# INF = int(1e9)
# n = int(input())
# m = int(input())
# graph = [[INF] * (n+1) for _ in range(n+1)]
#
# for a in range(1, n+1):
#     for b in range(1, n+1):
#         if a == b:
#             graph[a][b] = 0
#
# for _ in range(m):
#     a, b, c = map(int, input().split())
#     graph[a][b] = c
#
# for k in range(1, n+1):
#     for a in range(1, n+1):
#         for b in range(1, n+1):
#             graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b] )
#
# for a in range(1, n+1):
#     for b in range(1, n+1):
#         if graph[a][b] == INF:
#             print("INFINITY", end=" ")
#         else:
#             print(graph[a][b], end=" ")
#     print()

############################# question 1 #############################################
# n개 도시, 한 도시에서 출발 -> 다른 도시에 도착하는 m개 버스 있다. 모든 도시 쌍에 대해 필요한 최소 비용? 간선이 2개일 수도 있다. 같은 길인데.
# INF = int(1e9)
# n = int(input())
# m = int(input())
# graph = [[INF] * (n+1) for _ in range(n+1)]
#
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if i == j:
#             graph[i][j] = 0
#
# for _ in range(m):
#     a, b, c = map(int, input().split())
#     graph[a][b] = min(graph[a][b], c)
#
# for k in range(1, n+1):
#     for a in range(1, n+1):
#         for b in range(1, n+1):
#             graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
#
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if graph[i][j] == INF:
#             print("0", end=" ")
#         else:
#             print(graph[i][j], end=" ")
#     print()

################### Question 2 #############################################
#
# INF = int(1e9)
# n, m = map(int, input().split())
# graph = [[INF] * (n+1) for _ in range(n+1)]
#
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if i == j:
#             graph[i][j] = 0
#
# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[a][b] = 1
#
# for k in range(1, n+1):
#     for a in range(1, n+1):
#         for b in range(1, n+1):
#             graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
#
# c = 0
# for i in range(1, n+1):
#     check_in = 0
#     check_out = 0
#     for j in range(1, n+1):
#         if graph[i][j] != INF:
#             check_in += 1
#         if graph[j][i] != INF:
#             check_out += 1
#     if check_in + check_out == n-1:
#         c += 1
#
# print(c)

#################### Question 3 ####################################################################
# import heapq
# import sys
#
# input = sys.stdin.readline
# INF = int(1e9)
# ite = int(input())
#
# def djikstra(start):
#     x, y = start
#     q = []
#     heapq.heappush(q, (mapp[x][y], start))
#     distance[x][y] = mapp[x][y]
#     di_x = [0, 0, 1, -1]
#     di_y = [1, -1, 0, 0]
#     while q:
#         dist, now = heapq.heappop(q)
#         x_new, y_new = now
#         if distance[x_new][y_new] < dist:
#             continue
#         for o in range(4):
#             if 0 <= x_new + di_x[o] < len(mapp) and 0 <= y_new + di_y[o] < len(mapp[0]):
#                 cost = dist + mapp[x_new + di_x[o]][y_new + di_y[o]]
#                 if cost < distance[x_new + di_x[o]][y_new + di_y[o]]:
#                     distance[x_new + di_x[o]][y_new + di_y[o]] = cost
#                     heapq.heappush(q, (cost, (x_new + di_x[o], y_new + di_y[o])))
#
# for _ in range(ite):
#     n = int(input())
#     mapp = [[0] * n for _ in range(n)]
#     for i in range(n):
#         temp = list(map(int, input().split()))
#         for j in range(n):
#             mapp[i][j] = temp[j]
#
#     distance = [[INF] * n for _ in range(n)]
#     start = (0, 0)
#     djikstra(start)
#     print(distance[n-1][n-1])

#### Question 4 #############################################################
# 술래는 1번 부터 출발
# M개의 양방향 통로가 존재하며, 하나는 두 헛간 연결
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))

def djikstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for k in graph[now]:
            cost = dist + k[1]
            if cost < distance[k[0]]:
                distance[k[0]] = cost
                heapq.heappush(q, (cost, k[0]))

djikstra(1)
leng = int(1e9) * -1
num = -1
count = 1
for o in range(1, n+1):
    if distance[o] == leng:
        count += 1
    if distance[o] > leng:
        leng = distance[o]
        num = o
        count = 1

print(num, leng, count)