######## Question 1 ##########################3
# from collections import deque
#
#
# def bfs(graph, s, visited):
#     queue = deque([s])
#     #visited[s] = True
#     while queue:
#         now = queue.popleft()
#         for rest in graph[now]:
#             if visited[rest] == -1:
#                 queue.append(rest)
#                 visited[rest] = visited[now] + 1
#     return visited
#
#
# n, m, k, x = map(int, input().split())
# road = [[] for i in range(n+1)]
# for _ in range(m):
#     a, b = map(int, input().split())
#     road[a].append(b)
#
# visited = [-1] * (n+1)
# visited[x] = 0
# presence = False
# result = bfs(road, x, visited)
# for i in result:
#     if i == k:
#         print(result.index(i))
#         presence = True
#
# if presence == False:
#     print(-1)

####### Question 2 #####################################
# 0 빈칸, 1 벽, 2 바이러스       벽 3개 세우기 가능
# 퍼지고 난 뒤의 안전영역의 크기는?
#
# def spread(temp):
#     dx = [0, 0, 1, -1]
#     dy = [1, -1, 0, 0]
#     n2 =len(temp)
#     m2 = len(temp[0])
#     for i in range(n2):
#         for j in range(m2):
#             if temp[i][j] == 2:
#                 for k in range(4):
#                     dux = dx[k] + i
#                     duy = dy[k] + j
#                     if 0 <= dux < n2 and 0 <= duy < m2 and temp[dux][duy] == 0:
#                         temp[dux][duy] = 2
#                         spread(temp)
#     return temp
#
#
# def cases(mapp, temp):
#     global wall
#     global result
#     if wall == 3:
#         for p in range(len(mapp)):
#             for q in range(len(mapp[0])):
#                 temp[p][q] = mapp[p][q]
#         fin_map = spread(temp)
#         result_temp = 0
#         for k in range(len(fin_map)):
#             result_temp += fin_map[k].count(0)
#         result = max(result, result_temp)
#         return result
#
#     for i in range(len(mapp)):
#         for j in range(len(mapp[0])):
#             if mapp[i][j] == 0:
#                 mapp[i][j] = 1
#                 wall += 1
#                 cases(mapp, temp)
#                 wall -= 1
#                 mapp[i][j] = 0
#
#
# n, m = map(int, input().split())
# mapp = []
# temp = [[0] * m for _ in range(n)]
# for i in range(n):
#     mapp.append(list(map(int, input().split())))
#
# wall = 0
# result = 0
#
# cases(mapp, temp)
# print(result)

############ question 3 ######################################
# n, k = map(int, input().split())
# mapp = []
# for i in range(n):
#     mapp.append(list(map(int, input().split())))
# s, x, y = map(int, input().split())
#
#
# def spread(mapp, k, s):
#     dx = [0, 0, 1, -1]
#     dy = [1, -1, 0, 0]
#     x_axis = len(mapp)
#     y_axis = len(mapp[0])
#     for _ in range(s):
#         for c in range(1, k + 1):
#             for i in range(x_axis):
#                 for j in range(y_axis):
#                     if mapp[i][j] == c:
#                         for l in range(4):
#                             dux = dx[l] + i
#                             duy = dy[l] + j
#                             if 0 <= dux < x_axis and 0 <= duy < y_axis and mapp[dux][duy] == 0:
#                                 mapp[dux][duy] = -c
#             for i in range(x_axis):
#                 for j in range(y_axis):
#                     if mapp[i][j] < 0:
#                         mapp[i][j] = mapp[i][j] * -1
#     return mapp
#
# print(spread(mapp, k, s)[x-1][y-1])

#### question 4 ##############################################
from collections import deque
queue = deque([])

def right_word(w):
    count = 0
    if not w:
        return []
    if w[0] == ")":
        return False
    else:
        for i in range(len(w)):
            if w[i] == "(":
                count += 1
            else:
                count -= 1
        if count == 0:
            return True
        else:
            return False

def solution(p):
    left = 0
    right = 0
    temp = []
    word = list(p)
    if not word:
        return []
    for i in range(len(word)):
        if word[i] == "(":
            left += 1
        elif word[i] == ")":
            right += 1
        if left == right:
            u = word[0:i+1]
            v = word[i+1:]
            if right_word(u):
                return u + solution(v)
            else:
                temp.append("(")
                temp = temp + solution(v)
                temp.append(")")
                u.pop(0)
                u.pop()
                for k in range(len(u)):
                    if u[k] == "(":
                        u[k] = ")"
                    else:
                        u[k] = "("
                temp = temp + u
                return temp

result = solution("()))((()")
for i in range(len(result)):
    print(result[i], end='')










