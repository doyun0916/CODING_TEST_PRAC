################## Question 1 ###############################################
#
# import sys
# input = sys.stdin.readline
# arr = list(input())
# arr_new = []
# for i in range(len(arr)-1):
#     arr_new.append(int(arr[i]))
#
# mid = len(arr_new)//2
# s = 0
# f = len(arr_new) - 1
# left = 0
# right = 0
# for _ in range(mid):
#     left = left + arr_new[s]
#     right = right + arr_new[f]
#     s += 1
#     f -= 1
# if left == right:
#     print('LUCKY')
# else:
#     print('READY')

############# Question2 ###########################################################
# import sys
# input = sys.stdin.readline
# temp = list(input())
# temp.remove('\n')
# temp.sort()
# sum = 0
# r = 0
# try:
#     for i in range(len(temp)):
#         r = i
#         sum += int(temp[i])
# except:
#     for j in range(r, len(temp)):
#         print(temp[j], end='')
#     print(sum)

############# Question3 ##############################################################
# import sys
# input = sys.stdin.readline
# arr = list(input())
# arr.remove('\n')
# nu = []
# for i in range(1, len(arr)):
#     count = len(arr)//i
#     check = 1     # 같은 문자열이 몇번 반복되었는가.
#     start = 0     # 자르고자하는 문자열 시작
#     stop = i      # 자르고자하는 문자열 끝
#     temp = "".join(arr[start:stop])   # 기존 문자열
#     start += i
#     stop += i
#     fi = ""     # final 문자열
#     curr = None   # 현재 문자열
#     for j in range(count):
#         curr = "".join(arr[start:stop])
#         if len(curr) < i and curr != "":
#             fi = fi + temp + curr
#             break
#         if curr != temp:
#             if check > 1:
#                 fi = fi + str(check) + temp
#             else:
#                 fi = fi + temp
#             temp = curr
#             check = 1
#         else:
#             check += 1
#         start += i
#         stop += i
#     nu.append(len(fi))
# print(min(nu))

############ Question 4 ##########################################################
# NxN 홈,  열쇠 MxM 홈, 돌기
# 돌기-홈 x
# 2차원 배열 key, 2차원 배열 lock
# 열수 있으면 true, 없으면 false를 return!
# 0은 홈, 1은 돌기

# def solution(key, lock):
#     y = [1, -1, 0, 0]      # 오른, 왼, 위, 아래, 90오른
#     x = [0, 0, -1, 1]
#     x_base = 0
#     y_base = 0
#     INF = int(1e9)
#     x_dim = len(lock[0])
#     y_dim = len(lock)
#     lock_new = [[INF for _ in range(len(lock[0]) * 3)] for _ in range(len(lock) * 3)]
#     for i in range(x_dim):
#         for j in range(y_dim):
#             lock_new[i+3][j+3] = lock[i][j]
#
#     blank = 0
#     for i in range(len(lock)):
#         blank += lock[i].count(0)
#
#     for i in range(x_dim):
#         for j in range(y_dim):
#
#         if y_base > x_dim - 1:
#             y_base = 0
#             x_base += 1
#         for i in range()
#
#
#
#         y_base += 1
#
#     answer = True
#     return answer
#
# ####### 답 ###########            # 처음부터 다 체크! (4x4일때도 있으니까..!)
# def rotate_90(a):
#     n = len(a)
#     m = len(a[0])
#     result = [[0] * n for _ in range(m)]
#     for i in range(n):
#         for j in range(n):
#             result[j][n-1-i] = a[i][j]
#     return result
#
# def check(new_lock):
#     lock_length = len(new_lock) // 3
#     for i in range(lock_length, lock_length * 2):
#         for j in range(lock_length, lock_length * 2):
#             if new_lock[i][j] != 1:
#                 return False
#         return True
#
# def solution(key, lock):
#     n = len(lock)
#     m = len(key)
#     new_lock = [[0] * (n * 3) for _ in range(n*3)]
#     for i in range(n):
#         for j in range(n):
#             new_lock[i+n][j+n] = lock[i][j]
#
#     for rotation in range(4):
#         key = rotate_90(key)
#         for x in range(n * 2):
#             for y in range(n * 2):
#                 for i in range(m):
#                     for j in range(m):
#                         new_lock[x+i][y+j] += key[i][j]
#                 if check(new_lock) == True:
#                     return True
#                 for i in range(m):
#                     for j in range(m):
#                         new_lock[x+i][y+i] -= key[i][j]
#     return False
#
#
# ########### Question 5 #################################################################
# n = int(input())        #그리드
# k = int(input())        # 사과 개수
# app_lo = []           # 사과 위치 행, 열
# time = 0
# for _ in range(k):
#     a, b = map(int, input().split())
#     app_lo.append((a, b))
# l = int(input())         # 움직인 횟수
# sna_mov = []              # x초 후 왼쪽, 오른쪽 mov
# for _ in range(l):
#     a, b = input().split()
#     sna_mov.append((a, b))
#     if time < a:
#         time = a
#
# grid = [[0 for _ in range(n)] for _ in range(n)]
# for k in range(len(app_lo)):
#     for i in range(n):
#         for j in range(n):
#             if app_lo[k][0] == i and app_lo[k][1] == j:
#                 grid[i][j] = 1
#
# x_ori = 0
# y_ori = 0
# d = 0                                         # 오, 밑, 왼, 위
# mov = [(0, 1), (1, 0), (0, -1), (-1, 0)]             # 오, 밑, 왼, 위
# d_turn = [(1, 0), (0, -1), (-1, 0), (0, 1)]
# l_turn = [(-1, 0), (0, -1), (1, 0), (0, 1)]
# t = 0
# c = 0
#
# def movement(x_ori, y_ori, d, current):
#     if int(current[0]) + 1 == t:
#         if d == 0:
#             if current[1] == 'D':
#                 if d == 3:
#                     d = 0
#                 else:
#                     d += 1
#             else:
#                 if d == 0:
#                     d = 3
#                 else:
#                     d -= 1
#         if current[1] == 'D':
#             x_ori += d_turn[d][0]
#             y_ori += d_turn[d][1]
#         else:
#             x_ori += l_turn[d][0]
#             y_ori += l_turn[d][1]
#     else:
#         x_ori += mov[0][0]
#         y_ori += mov[0][1]
#
# while True:
#     current = sna_mov[c]
#     if x_ori > n or x_ori < 0 or y_ori > n or y_ori < n:
#         break
#     t += 1
#
#
# ##### 답 #############
# n = int(input())
# k = int(input())
# data = [[0] * (n + 1) for _ in range(n+1)]
# info = []
# for _ in range(k):
#     a, b = map(int, input().split())
#     data[a][b] = 1
#
# l = int(input())
# for _ in range(l):
#     x, c = input().split()
#     info.append((int(x), c))
#
# dx = [0, 1, 0, -1]
# dy = [1, 0, -1, 0]
#
# def turn(direction, c):
#     if c == 'L':
#         direction = (direction - 1) % 4
#     else:
#         direction = (direction + 1) % 4
#     return direction
#
# def simulate():
#     x, y = 1, 1
#     data[x][y] = 2
#     direction = 0
#     time = 0
#     index = 0
#     q = [(x, y)]
#     while True:
#         nx = x + dx[direction]
#         ny = y + dy[direction]
#         if 1 <= nx and nx <= n and 1 <= ny and data[nx][ny] != 2:
#             if data[nx][ny] == 0:
#                 data[nx][ny] = 2
#                 q.append((nx, ny))
#                 px, py = q.pop(0)
#                 data[px][py] = 0
#             if data[nx][ny] == 1:
#                 data[nx][ny] = 2
#                 q.append((nx, ny))
#         else:
#             time += 1
#             break
#         x, y = nx, ny
#         time += 1
#         if index < l and time == info[index][0]:
#             direction = turn(direction, info[index][1])
#             index += 1
#     return time
#
# print(simulate())

########################################## Question 6 ###############################################################

# [x, y, 0 기둥 1 보, 0 삭제 1 설치]
# 바닥에 기둥부터 설치, 벽면을 벗어나면 x 기둥, 보 둘다.\
# 보는 오른쪽, 기둥은 위로 설치 or 삭제
# return [x, y, a] = > x, y는 교차점, a = 0 기둥, 1 보
# x 기준 오름차순 정렬, x가 같으면, y기준 오름차순 정렬. x, y다 같으면 기둥 먼저
# 설치 1

# q = []
# def solution(n, build_frame):
#     b_map = [[0] * (n+1) for _ in range(n+1)]
#     for i in range(len(build_frame)):
#         if build_frame[i][2] == 0:
#             if build_frame[i][3] == 1:                                  # 기둥 설치
#                 b_map[build_frame[i][0]][build_frame[i][1]] = 1
#                 q.append((build_frame[i][0], build_frame[i][1], build_frame[i][2]))
#             else:                                                      # 기둥 삭제시
#                 if b_map[build_frame[i][0]+1][build_frame[i][1]] == 1:
#                     if b_map[build_frame[i][0]][build_frame[i][1]-1] == 1 and b_map[build_frame[i][0]][build_frame[i][1]+1] == 1:
#                         b_map[build_frame[i][0]][build_frame[i][1]] = 0
#                         q.remove((build_frame[i][0], build_frame[i][1], build_frame[i][2]))
#                     else:
#                         continue
#                 else:
#                     continue
#         else:
#             if build_frame[i][3] == 1:                                           # 보 설치
#                if b_map[build_frame[i][0]-1][build_frame[i][1]] == 1:
#                    b_map[build_frame[i][0]][build_frame[i][1]] = 1
#                    q.append((build_frame[i][0], build_frame[i][1], build_frame[i][2]))
#             else:                                                    # 보 삭제
#                 if b_map[build_frame[i][0]][build_frame[i][1]-1] == 1 and b_map[build_frame[i][0]][build_frame[i][1]+1] == 1:
#                     b_map[build_frame[i][0]][build_frame[i][1]] = 0
#                     q.remove((build_frame[i][0], build_frame[i][1], build_frame[i][2]))
#
# solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1], [2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]])
# print(q)
#
#     #answer = [[]]
#     #return answer
#
# ###### 답 #########################################
#
# def possible(answer):
#     for x, y, stuff in answer:
#         if stuff == 0:
#             if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer:
#                 continue
#             else:
#                 return False
#         elif stuff == 1:
#             if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
#                 continue
#             else:
#                 return False
#     return True
#
# def solution(n, build_frame):
#     answer = []
#     for frame in build_frame:
#         x, y, stuff, operate = frame
#         if operate == 0:
#             answer.remove([x, y, stuff])
#             if not possible(answer):
#                 answer.append([x, y, stuff])
#         if operate == 1:
#             answer.append([x, y, stuff])
#             if not possible(answer):
#                 answer.remove([x, y, stuff])
#     return sorted(answer)

 ## 핵심! 1. 2차원 그릴 필요가 없다. 2. 크게 다 돌려본다. 3. 심플하게 일단 수도로 함수화 시켜본다.

#### question 7 ###################################################

# 빈칸 0, 치킨집 2, 집 1 (행,열) r,c 는 1부터
# 치킨 거리 = 집과 가장 가까운 치킨집 사이의 거리
# 도시의 치킨 거리 = 모든 집의 치킨 거리의 합
# 가장 수익을 많이 낼 수 있는 치킨집의 개수는 최대 M개
# 도시의 치킨 거리가 가장 작게 될지 구하는 프로그램 작성!
#
#
# n, m = map(int, input().split())
# mapp = []
# for i in range(n):
#     ro = list(map(int, input().split()))
#     mapp.append(ro)
#
# shortest = 0
# chicken_len = []
# def check(mappp, i, j):
#     temp = []
#     for p in range(n):
#         for q in range(n):
#             if mappp[p][q] == 2:
#                 temp.append(abs(p - i) + abs(q - j))
#     return temp
#
# def final(chicken_len):
#     while True:
#         temp = []
#         comp = -1
#         len_result = 0
#         len_sum = 0
#         for i in range(len(chicken_len)):
#             temp2 = max(chicken_len[i])
#             len_sum += temp2
#             temp.append(temp2)
#             if chicken_len[i].index(max(chicken_len[i])) != comp:
#                 len_result += 1
#                 comp = temp2
#         if len_result == m:
#             break
#         ind = temp.index(max(temp))
#         while True:
#             if len(chicken_len[ind]) == 1:
#                 temp.remove(max(temp))
#                 ind = temp.index(max(temp))
#             else:
#                 chicken_len[ind].remove(max(temp))
#                 break
#
#     return len_sum
#
# for i in range(n):
#     for j in range(n):
#         if mapp[i][j] == 1:
#             chicken_len.append(check(mapp, i, j))
#
# print(final(chicken_len))

############# 답 ##########################################################
# from itertools import combinations
#
# n, m = map(int, input().split())
# chicken, house = [], []
#
# for r in range(n):
#     data = list(map(int, input().split()))
#     for c in range(n):
#         if data[c] == 1:
#             house.append((r, c))  # 집
#         elif data[c] == 2:
#             chicken.append((r, c))  # 치킨 집
#
# # 모든 치킨집에서 m개의 치킨집을 뽑는 조합 계산
# candidates = list(combinations(chicken, m))
#
# def get_sum(candidate):
#     result = 0
#     for hx, hy in house:
#         temp = 1e9
#         for cx, cy in candidate:
#             temp = min(temp, abs(hx-cx) + abs(hy-cy))
#         result += temp
#     return result
#
# result = 1e9
# for candidate in candidates:
#     result = min(result, get_sum(candidate))
#
# print(result)
#

########### Question 8 ##############################################
import copy

def solution(n, weak, dist):
    mapp = [0] * 2*n
    for i in range(len(weak)):
        for j in range(0, 2*n, 2):
            if j//2 == weak[i]:
                mapp[j] = 1
                break

    dist.sort(reverse=True)
    minimum = int(1e9)
    fr = 0
    weakest = 0
    for i in dist:
        for k in range(n*2):
            mapp_dup = copy.deepcopy(mapp)
            for j in range(i*2):
                if mapp_dup[(k + j) % n*2] == 1:
                    mapp_dup[(k + j) % n*2] = 0
            if minimum > mapp_dup.count(1):
                minimum = mapp_dup.count(1)
                weakest = k
        for j in range(i*2):
            if mapp[(weakest + j) % n*2] == 1:
                mapp[(weakest + j) % n*2] = 0
        fr += 1
        if mapp.count(1) == 0:
            break
    answer = fr
    return answer

print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))