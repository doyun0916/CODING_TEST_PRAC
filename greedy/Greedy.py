# # Q1 #
# # 공포도 x 모험가는 x명 이상 구성한 모험가 그룹에 참여. 최대 그룹 몇개 가능? 몇명은 남아 있어도 됨.
# n = int(input())
# charact = list(map(int, input().split()))
# charact.sort(reverse=True)
# group = 0
# count = 0
# now = charact[0]
# for i in range(len(charact)):
#     count += 1
#     if count == now:
#         if i+1 < len(charact):
#             now = charact[i+1]
#         count = 0
#         group += 1
#
# print(group)

# # Q2 #
# n = list(map(int, input()))
# result = 1
# for i in n:
#     if i == 0:
#         continue
#     else:
#         result = result * i
#
# print(result)

# Q3 #
# m = list(map(int, input()))
# a = m.count(0)
# b = m.count(1)
# check = True
# count = 0
# if a > b:
#     for i in range(len(m)):
#         if check == False:
#             count += 1
#         if m[i] == 1:
#             m[i] = 0
#             if i + 1 < len(m):
#                 if m[i+1] != m[i]:
#                     check = False
#                 else:
#                     check = True
# else:
#     for i in range(len(m)):
#         if check == False:
#             count += 1
#         if m[i] == 0:
#             m[i] = 1
#             if i + 1 < len(m):
#                 if m[i+1] != m[i]:
#                     check = False
#                 else:
#                     check = True
#
# print(count)

# # Q4 #
# n개를 이용하여 만들 수 없는 양의 정수중 최솟값!
# n = int(input())
# data = list(map(int, input().split()))
# data.sort()
#
# target = 1
# for x in data:
#     if target < x:
#         break
#     target += x
#
# print(target)

## Q5 ##
from itertools import combinations
n, m = map(int, input().split())
balls = list(map(int, input().split()))
balls_num = []
for i in range(len(balls)):
    balls_num.append((balls[i], i+1))
combs = list(combinations(balls_num, 2))
count = 0
for i in range(len(combs)):
    if combs[i][0][0] == combs[i][1][0]:
        count += 1
print(len(combs) - count)

## Q6 ##

def solution(food_times, k):
    time = 0
    t = 0
    while time != k:
        if food_times[t % 3] != 0:
            food_times[t % 3] -= 1
            t += 1
            time += 1
        else:
            t += 1

    if food_times.count(0) == len(food_times):
        answer = -1
    else:
        answer = t % 3 + 1
    return answer

