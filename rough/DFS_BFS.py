## Q15 ##
# from collections import deque
# n, m, k, x = map(int, input().split())
# graph = [[] for _ in range(n+1)]
# for i in range(m):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#
# visited = [False] * (n+1)
#
# def bfs(graph, start, visited, k):
#     result = []
#     length = 0
#     q = deque([(start, length)])
#     visited[start] = True
#     while q:
#         v, leng = q.popleft()
#         if leng == k:
#             result.append(v)
#         leng += 1
#         for i in graph[v]:
#             if not visited[i]:
#                 q.append((i, leng))
#                 visited[i] = True
#
#     return result
#
# final = bfs(graph, x, visited, k)
# final.sort()
# if not final:
#     print(-1)
# else:
#     for i in final:
#         print(i)

## Q16 ## 안전영역의 크기 최대값구하기 벽은 3개
# from itertools import combinations
# from copy import deepcopy
# n, m = map(int, input().split())
# blank = []
# mapp = []
# for i in range(n):
#     temp = list(map(int, input().split()))
#     mapp.append(temp)
#     for j in range(m):
#         if temp[j] == 0:
#             blank.append((i, j))
# def virus(x, y):
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 0 <= nx < n and 0 <= ny < m:
#             if mapp_temp[nx][ny] == 0:
#                 mapp_temp[nx][ny] = 2
#                 virus(nx, ny)
# dx = [0, 0, 1, -1]
# dy = [1, -1, 0, 0]
# blank_comb = list(combinations(blank, 3))
# final = []
# for combi in blank_comb:
#     result = 0
#     mapp_temp = deepcopy(mapp)
#     for i in combi:
#         mapp_temp[i[0]][i[1]] = 1
#     for q in range(n):
#         for p in range(m):
#             if mapp_temp[q][p] == 2:
#                 virus(q, p)
#     for i in range(n):
#         result += mapp_temp[i].count(0)
#     final.append(result)
#
# print(max(final))

# ## Q17 ##
# n, k = map(int, input().split())
# mapp = []
# virus = []
# for i in range(n):
#     temp = list(map(int, input().split()))
#     mapp.append(temp)
#     for j in range(n):
#         if temp[j] != 0:
#             virus.append((temp[j], i, j))
#
# s, x, y = map(int, input().split())
# dx = [0, 0, 1, -1]
# dy = [1, -1, 0, 0]
#
# virus_next = []
# for k in range(s):
#     virus.sort()
#     for h in range(len(virus)):
#         num, x_temp, y_temp = virus[h]
#         for q in range(4):
#             dx_temp = x_temp + dx[q]
#             dy_temp = y_temp + dy[q]
#             if 0 <= dx_temp < n and 0 <= dy_temp < n:
#                 if mapp[dx_temp][dy_temp] == 0:
#                     mapp[dx_temp][dy_temp] = num
#                     virus_next.append((num, dx_temp, dy_temp))
#     virus = virus_next
# print(mapp[x-1][y-1])

## Q18 ##
# def balanced_index(p):
#     count = 0
#     for i in range(len(p)):
#         if p[i] == '(':
#             count += 1
#         else:
#             count -= 1
#         if count == 0:
#             return i
#
# def check_proper(p):
#     count = 0
#     for i in p:
#         if i == '(':
#             count += 1
#         else:
#             if count == 0:         # 열린게 없는데 닫아버린다고?
#                 return False        # return False
#             count -= 1
#         return True
#
# def solution(p):
#     answer = ''
#     if p == '':
#         return answer
#     index = balanced_index(p)
#     u = p[:index +1]
#     v = p[index + 1:]
#     if check_proper(u):
#         answer = u + solution(v)
#     else:
#         answer = '('
#         answer += solution(v)
#         answer += ')'
#         u = list(u[1:-1])
#         for i in range(len(u)):
#             if u[i] == '(':
#                 u[i] = ')'
#             else:
#                 u[i] = '('
#         answer += "".join(u)
#     return answer

## Q19 ##
# from itertools import permutations
#
# n = int(input())
# nums = list(map(int, input().split()))
# op = list(map(int, input().split()))
# operators = []
# for i in range(4):
#     for _ in range(op[i]):
#         if i == 0:
#             operators.append('+')
#         elif i == 1:
#             operators.append('-')
#         elif i == 2:
#             operators.append('*')
#         else:
#             operators.append('//')
#
# operators_var = list(permutations(operators, (n-1)))
#
# minimum = int(1e9)
# maximum = -int(1e9)
# for ops in operators_var:
#     temp = nums[0]
#     for q in range(len(ops)):
#         if ops[q] == '+':
#             temp += nums[q+1]
#         elif ops[q] == '-':
#             temp -= nums[q+1]
#         elif ops[q] == '*':
#             temp = temp * nums[q+1]
#         else:
#             temp = int(temp / nums[q+1])
#     minimum = min(minimum, temp)
#     maximum = max(maximum, temp)
#
# print(minimum, maximum)

## Q20 ##
# from itertools import combinations
# from copy import deepcopy
# n = int(input())
# students = []
# teachers = []
# candidates = []
# mapp = []
# for i in range(n):
#     temp = list(input().split())
#     mapp.append(temp)
#     for j in range(n):
#         if temp[j] == 'T':
#             teachers.append((i, j))
#         elif temp[j] == 'X':
#             candidates.append((i, j))
#
# candi = list(combinations(candidates, 3))
# dx = [0, 0, 1, -1]
# dy = [1, -1, 0, 0]
#
#
# for can in candi:
#     xy1, xy2, xy3 = can
#     mapp_temp = deepcopy(mapp)
#     mapp_temp[xy1[0]][xy1[1]] = 'O'
#     mapp_temp[xy2[0]][xy2[1]] = 'O'
#     mapp_temp[xy3[0]][xy3[1]] = 'O'
#     possibility = True
#     for i in teachers:
#         x, y = i
#         for j in range(4):
#             c = 1
#             while True:
#                 x_temp = x + (dx[j] * c)
#                 y_temp = y + (dy[j] * c)
#                 if 0 <= x_temp < n and 0 <= y_temp < n:
#                     if mapp_temp[x_temp][y_temp] == 'S':
#                         possibility = False
#                         break
#                     elif mapp_temp[x_temp][y_temp] == 'O':
#                         break
#                     else:
#                         c += 1
#                 else:
#                     break
#         if possibility:
#             print('YES')
#             exit()
#
# print('NO')

## Q21 ##
from collections import deque
n, l, r = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
result = 0

def process(x, y, index):
    united = []
    united.append((x,y))
    q = deque()
    q.append((x, y))
    union[x][y] = index
    summary = graph[x][y]
    count = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
                if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                    q.append((nx, ny))
                    union[nx][ny] = index
                    summary += graph[nx][ny]
                    count += 1
                    united.append((nx, ny))
    for i, j in united:
        graph[i][j] = summary // count
        return count

total_count = 0

while True:
    union = [[-1] * n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1:
                process(i, j, index)
                index += 1
    if index == n * n:
        break
    total_count += 1

print(total_count)

## Q22 ## *******************************************
def solution(board):
    answer = 0
    return answer