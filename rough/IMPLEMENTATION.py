# ## Q7 ##
# num = list(map(int, input()))
# forw = num[:len(num)//2]
# back = num[len(num)//2:]
# if sum(forw) == sum(back):
#     print("LUCKY")
# else:
#     print("READY")

## Q8 ##
# character = list(input())
# chara = []
# num = []
# for i in character:
#     if i.isalpha():
#         chara.append(i)
#     else:
#         num.append(int(i))
# chara.sort()
# result = chara.append(str(sum(num)))
# final = "".join(chara)
# print(final)

# ## Q9 ##
# def solution(s):
#     answer = len(s)
#     for step in range(1, len(s) // 2 + 1):
#         compressed = ""
#         prev = s[0: step]
#         count = 1
#         for j in range(step, len(s), step):
#             if prev == s[j:j + step]:
#                 count += 1
#             else:
#                 compressed += str(count) + prev if count >= 2 else prev
#                 prev = s[j:j + step]
#                 count = 1
#         compressed += str(count) + prev if count >= 2 else prev
#         answer = min(answer, len(compressed))
#     return answer
# print(solution("aabbaccc"))

## Q10 ##
# def rotate(x):
#     row = len(x)
#     col = len(x[0])
#     for i in range(row):
#         for j in range(col):
#             x[i][j] = x[col - j - 1][i]
#     return x
# def solution(key, lock):
#     row = len(lock)
#     col = len(lock[0])
#     lock_new = [[1] * (col*3) for _ in range(row*3)]
#     state = True
#     for i in range(row):
#         for j in range(col):
#             lock_new[i+3][j+3] = lock[i][j]
#     dx = [0, 1]      # 동남
#     dy = [1, 0]
#     for _ in range(len(lock_new) * len(lock_new[0])):
#         for k in range(4):
#             key = rotate(key)
#             for x in range(row * 2):
#                 for y in range(row * 2):
#                     for i in range(row):
#                         for j in range(col):
#                             lock_new[x+i][y+j] += key[i][j]
#
#                     for i in range(row):
#                         for j in range(col):
#                             if lock_new[i + row][j + col] == 0:
#                                 state = False
#                                 break
#                     if state:
#                         answer = True
#                         return answer
#                     else:
#                         state = True
#
#                     for i in range(row):
#                         for j in range(col):
#                             lock_new[x+i][y+j] -= key[i][j]
#     answer = False
#     return answer
#
# print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
#
## Q11 ##
### x초 끝난뒤에, 왼쪽(L) or 오른쪽(D)으로 90도 회전
# from collections import deque
# n = int(input())
# board = [[0] * n for _ in range(n)]
# apple_num = int(input())
# for _ in range(apple_num):
#     a, b = map(int, input().split())
#     board[a-1][b-1] = 1
# dir_num = int(input())
# snake = deque()
# directions = []
# dx = [0, 0, 1, -1]
# dy = [1, -1, 0, 0]
# way = 0
# for _ in range(dir_num):
#     a, b = input().split()
#     directions.append((int(a), b))
# snake.append((0, 0))
# tim = 0
# for i in range(len(directions)):
#     turn = False
#     while True:
#         if tim == directions[i][0]:
#             if way%4 == 3:
#                 if directions[i][1] == "D":
#                     way = abs((way + 1)%4)
#                 else:
#                     way = abs((way + 2)%4)
#             elif way%4 == 2:
#                 if directions[i][1] == "D":
#                     way = abs((way - 1)%4)
#                 else:
#                     way = abs((way - 2)%4)
#             elif way%4 == 0:
#                 if directions[i][1] == "D":
#                     way = abs((way + 2)%4)
#                 else:
#                     way = abs((way + 3)%4)
#             elif way%4 == 1:
#                 if directions[i][1] == "D":
#                     way = abs((way - 2)%4)
#                 else:
#                     way = abs((way - 3)%4)
#             turn = True
#
#         head_x, head_y = snake[0]
#         dx_temp = head_x + dx[way]
#         dy_temp = head_y + dy[way]
#         if 0 <= dx_temp < n and 0 <= dy_temp < n:
#             if (dx_temp, dy_temp) in snake:
#                 tim += 1
#                 print(tim)
#                 exit()
#             else:
#                 snake.appendleft((dx_temp, dy_temp))
#                 tim += 1
#                 if board[dx_temp][dy_temp] != 1:
#                     tail_x, tail_y = snake.pop()
#                     board[tail_x][tail_y] = 0
#                 board[dx_temp][dy_temp] = 2
#             if turn and i != (len(directions) - 1):
#                 break
#         else:
#             tim += 1
#             print(tim)
#             exit()

## Q12 ##
# 벽면의 크기 n
# [x,y,a,b] = 설치 또는 삭제 좌표(x, y), a(0 기둥- 위쪽으로, 1 보-오른쪽으로), b(0 삭제, 1 설치)
# return [x,y,a], x,y,a 순으로 정렬
#
# def check_x_axis(gidung, x):
#     for i in range(len(gidung)):
#         if gidung[i][0] == x:
#             return True
#     return False
#
# def solution(n, build_frame):
#     gidung = []
#     bo = []
#     for frame in build_frame:
#         x, y, a, b = frame
#         if b == 1:
#             if a == 0:
#                 if (y == 0) or ((x, y, 1) in bo) or ((x-1, y, 1) in bo) or ((x, y-1, 0) in gidung):
#                     gidung.append((x, y, 0))
#             else:
#                 if check_x_axis(gidung, x) or check_x_axis(gidung, x+1) or ((x-1, y, 1) in bo and (x+1, y, 1) in bo):
#                     bo.append((x, y, 1))
#         else:
#             if a == 0:
#                 if (x, y+1, 1) in bo:
#                     if (x-1, y+1, 1) in bo and (x+1, y+1, 1) in bo:
#                         gidung.remove((x, y, 0))
#                 elif (x-1, y+1, 1) in bo:
#                     if (x, y+1, 1) in bo and (x-1-1, y+1, 1) in bo:
#                         gidung.remove((x, y, 0))
#                 #elif (x, y+1) not in gidung:
#                     #gidung.remove((x, y))
#             else:
#                 if ((x-1, y, 1) in bo) and ((x+1, y, 1) in bo):
#                     if ((x - 1, y, 1) in bo) and (check_x_axis(gidung, x - 1) or check_x_axis(gidung, x)) and ((x + 1, y, 1) in bo) and (check_x_axis(gidung, x+1) or check_x_axis(gidung, x+1+1)):
#                         bo.remove((x, y, 1))
#     return gidung, bo
#
# g, b = solution(5, [[0,0,0,1], [2,0,0,1], [4,0,0,1], [0,1,1,1], [1,1,1,1], [2,1,1,1], [3,1,1,1], [2,0,0,0], [1,1,1,0], [2,2,0,1]])
# result = g + b
# result.sort(key=lambda x: (x[0], x[1], x[2]))
# print(result)

## Q13 ##
# 빈칸 0, 치킨집 2, 집 1    도시(r,c)
# 모든 집의 치킨거리 합 = 도시의 치킨거리
# 두칸 사이 거리 => abs(x1 - x2) + abs(y1 - y2)
# 치킨집 n개 고르고 페쇄! 도시 치킨거리 가장 작도록 한다.
# from itertools import combinations
# import copy
# n, m = map(int, input().split())
# chicken_house = []
# INF = int(1e9)
# mapp = [[0] * n for _ in range(n)]
# for i in range(n):
#     data = list(map(int, input().split()))
#     for j in range(n):
#         if data[j] == 1:
#             mapp[i][j] = INF
#         elif data[j] == 2:
#             chicken_house.append((i, j))
#             mapp[i][j] = 0
#         else:
#             mapp[i][j] = data[j]
#
# samples = list(combinations(chicken_house, m))
# final = []
# for sample in samples:
#     test_mapp = copy.deepcopy(mapp)
#     result = 0
#     for position in sample:
#         x, y = position
#         for i in range(n):
#             for j in range(n):
#                 if test_mapp[i][j] > 0:
#                     test_mapp[i][j] = min(test_mapp[i][j], (abs(i-x) + abs(j-y)))
#
#     for i in range(n):
#         result += sum(test_mapp[i])
#     final.append(result)
#
# print(min(final))

## Q14 ##
#둘레 n, 시간 1시간, 출발부터 시계 or 반시계로 감. 친구 수의 최솟값 return, 불다능 -1
from copy import deepcopy


def solution(n, weak, dist):
    mapp = [0] * n
    for point in weak:
        mapp[point] = 1
    dist.sort(reverse=True)
    mapp_test = deepcopy(mapp)
    p_num = 0
    for length in dist:
        p_num += 1
        temp = []
        for point in weak:
            count_front = 0
            count_reverse = 0
            for i in range(length + 1):
                if mapp_test[(point + i) % n] == 1:
                    count_front += 1
                if mapp_test[(point - i)] == 1:
                    count_reverse += 1
            if count_front > count_reverse:
                temp.append((count_front, point, "front", length + 1))
            else:
                temp.append((count_reverse, point, "reverse", length + 1))
        c, p, d, l = max(temp)
        for k in range(l):
            if d == "front":
                mapp_test[(p + k) % 12] = 0
            else:
                mapp_test[(p - k)] = 0

        if mapp_test.count(1) == 0:
            break

    print(p_num)
solution(12, [1, 3, 4, 9, 10], [3, 5, 7])
