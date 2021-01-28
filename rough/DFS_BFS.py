######## Question 1 ##########################3
# from collections import deque
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
# from collections import deque
# queue = deque([])
#
# def right_word(w):
#     count = 0
#     if not w:
#         return []
#     if w[0] == ")":
#         return False
#     else:
#         for i in range(len(w)):
#             if w[i] == "(":
#                 count += 1
#             else:
#                 count -= 1
#         if count == 0:
#             return True
#         else:
#             return False
#
# def solution(p):
#     left = 0
#     right = 0
#     temp = []
#     word = list(p)
#     if not word:
#         return []
#     for i in range(len(word)):
#         if word[i] == "(":
#             left += 1
#         elif word[i] == ")":
#             right += 1
#         if left == right:
#             u = word[0:i+1]
#             v = word[i+1:]
#             if right_word(u):
#                 return u + solution(v)
#             else:
#                 temp.append("(")
#                 temp = temp + solution(v)
#                 temp.append(")")
#                 u.pop(0)
#                 u.pop()
#                 for k in range(len(u)):
#                     if u[k] == "(":
#                         u[k] = ")"
#                     else:
#                         u[k] = "("
#                 temp = temp + u
#                 return temp
#
# result = solution("()))((()")
# for i in range(len(result)):
#     print(result[i], end='')

########## Question 5 ##################################################
# n = int(input())
# data = list(map(int, input().split()))
# add, sub, mul, div = map(int, input().split())
# min_val = int(1e9)
# max_val = int(-1e9)
# i = 0
# def cal(data, now):
#     global min_val, max_val, add, sub, mul, div, i
#     if i == n-1:
#         min_val = min(min_val, now)
#         max_val = max(max_val, now)
#         return
#     if add > 0:
#         add -= 1
#         i += 1
#         cal(data, now + data[i])
#         i -= 1
#         add += 1
#     if sub > 0:
#         sub -= 1
#         i += 1
#         cal(data, now - data[i])
#         i -= 1
#         sub += 1
#     if mul > 0:
#         mul -= 1
#         i += 1
#         cal(data, now * data[i])
#         i -= 1
#         mul += 1
#     if div > 0:
#         div -= 1
#         i += 1
#         cal(data, int(now / data[i]))
#         i -= 1
#         div += 1
#
# cal(data, data[0])
# print(max_val, min_val)

######### Question 6 ##################################################
#선생 T, 학생 S, 장애 O
# 장애물 3개 설치해야함. 모든 학생이 피할 수 있어야함. 가능하면 yes else no
# n = int(input())
# mapp = []
# for i in range(n):
#     mapp.append(list(input().split()))
# #mapp_test = [[0] * n for _ in range(n)]
# i = 0
# c = 0
# def student_check(mapp):
#     dx = [0, 0, 1, -1]
#     dy = [1, -1, 0, 0]
#     n = len(mapp)
#     for i in range(n):
#         for j in range(n):
#             if mapp[i][j] == 'T':
#                 dirx = i
#                 diry = j
#                 while True:
#                     dix = dirx
#                     diy = diry
#                     while diy < n:
#                         if mapp[dix][diy] == 'O':
#                             break
#                         if mapp[dix][diy] == 'S':
#                             return False
#                         dix += dx[0]
#                         diy += dy[0]
#                     dix = dirx
#                     diy = diry
#                     while diy >= 0:
#                         if mapp[dix][diy] == 'O':
#                             break
#                         if mapp[dix][diy] == 'S':
#                             return False
#                         dix += dx[1]
#                         diy += dy[1]
#                     dix = dirx
#                     diy = diry
#                     while dix < n:
#                         if mapp[dix][diy] == 'O':
#                             break
#                         if mapp[dix][diy] == 'S':
#                             return False
#                         dix += dx[2]
#                         diy += dy[2]
#                     dix = dirx
#                     diy = diry
#                     while dix >= 0:
#                         if mapp[dix][diy] == 'O':
#                             break
#                         if mapp[dix][diy] == 'S':
#                             return False
#                         dix += dx[3]
#                         diy += dy[3]
#                     break
#     return True
#
# def check(mapp):
#     #global mapp_test
#     global c
#     for p in range(n):
#         for q in range(n):
#             if c == 3:
#                 if student_check(mapp):
#                     return 'Yes'
#                 mapp[p][q-1] = 'X'
#                 c -= 1
#             if mapp[p][q] == 'X':
#                 mapp[p][q] = 'O'
#                 c += 1
#                 check(mapp)
#     return 'No'
#
# print(check(mapp))
#
# #### 답 ##########
# from itertools import combinations
#
# n = int(input())
# board = []
# teachers = []
# spaces = []
#
# for i in range(n):
#     board.append(list(input().split()))
#     for j in range(n):
#         if board[i][j] == 'T':
#             teachers.append((i, j))
#         if board[i][j] == 'X':
#             spaces.append((i, j)
#
# def watch(x, y, direction):
#     if direction == 0:
#         while y >= 0:
#             if board[x][y] == 'S':
#                 return True
#             if board[x][y] == 'O':
#                 return False
#             y -= 1
#     if direction == 1:
#         while y < n:
#             if board[x][y] == 'S':
#                 return True
#             if board[x][y] == 'O':
#                 return False
#             y += 1
#     if direction == 2:
#         while x >= 0:
#             if board[x][y] == 'S':
#                 return True
#             if board[x][y] == 'O':
#                 return False
#             x -= 1
#     if direction == 3:
#         while x < n:
#             if board[x][y] == 'S':
#                 return True
#             if board[x][y] == 'O':
#                 return False
#             x += 1
#     return False
#
# def process():
#     for x,y in teachers:
#         for i in range(4):
#             if watch(x, y, i):
#                 return True
#     return False
#
# find = False
#
# for data in combinations(spaces, 3):
#     for x, y in data:
#         board[x][y] = '0'
#     if not process():
#         find = True
#         break
#     for x, y in data:
#         board[x][y] = 'X'
#
# if find:
#     print('Yes')
# else:
#     print('No')

########################## Question 7 #############################################################################
# 국경선 공유(동서남북) 두 나라 인구 차이가 L명, R명 이하면, 국경선 하루동안 안염.
# 위에 따라 국경선 다 연다.
#
# n, l, r = map(int, input().split())
# mapp = []
# for _ in range(n):
#     mapp.append(list(map(int, input().split())))
# location = []
# population = []
# dx = [0, 0, 1, -1]
# dy = [1, -1, 0, 0]
# for i in range(n):
#     for j in range(n):
#         location.append((i,j))
#         population.append(mapp[i][j])
#         for k in range(4):
#             dtx = i + dx[k]
#             dty = j + dy[k]
#             if l <= abs(mapp[i][j] - mapp[dtx][dty]) <= r:
#                 location.append((dtx, dty))
#                 population.append(mapp[dtx][dty])

############# Question 9 ######################################################################################

from collections import deque
def get_next_pos(pos, board):
    pos_new = []
    pos = list(pos)
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    p1x, p1y, p2x, p2y = pos[0][0], pos[0][1], pos[1][0], pos[1][1]
    for i in range(4):
        if board[p1x + dx[i]][p1y + dy[i]] != 1 and board[p2x + dx[i]][p2y + dy[i]] != 1:
            pos_new.append({(p1x + dx[i], p1y + dy[i]), (p2x + dx[i], p2y + dy[i])})

    if p1x == p2x:
        for i in [-1, 1]:
            if board[p1x + i][p1y] == 0 and board[p2x + i][p2y] == 0:
                pos_new.append({(p1x, p1y), (p2x + i, p1y)})
                pos_new.append({(p2x, p2y), (p1x + i, p2y)})

    elif p1y == p2y:
        for i in [-1, 1]:
            if board[p1x][p1y + i] == 0 and board[p2x][p2y + i] == 0:
                pos_new.append({(p1x, p1y), (p1x, p2y + i)})
                pos_new.append({(p2x, p2y), (p2x, p1y + i)})

    return pos_new

def solution(board):
    n = len(board)
    mapp = [[1] * (n+2) for i in range(n+2)]
    for i in range(n):
        for j in range(n):
            mapp[i+1][j+1] = board[i][j]
    visited = []
    post = {(1, 1), (1, 2)}
    queue = deque()
    queue.append((post, 0))
    visited.append({(1, 1), (1, 2)})
    while queue:
        pos, cost = queue.popleft()
        if (n, n) in pos:
            return cost
        for next_pos in get_next_pos(pos, mapp):
            if next_pos not in visited:
                queue.append((next_pos, cost+1))
                visited.append(next_pos)


print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]))

