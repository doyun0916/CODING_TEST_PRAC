####### Question 1 ########################
# t = int(input())
# def find_next(mapp, curr):
#     case = []
#     case_ind = []
#     x, y = curr
#     if 0 <= x-1 < len(mapp) and 0 <= y + 1 < len(mapp[0]):
#         case.append(mapp[x - 1][y + 1])
#         case_ind.append((x-1, y+1))
#     if 0 <= x < len(mapp) and 0 <= y + 1 < len(mapp[0]):
#         case.append(mapp[x][y + 1])
#         case_ind.append((x, y + 1))
#     if 0 <= x + 1 < len(mapp) and 0 <= y + 1 < len(mapp[0]):
#         case.append(mapp[x + 1][y + 1])
#         case_ind.append((x + 1, y + 1))
#     print(case)
#     fin = max(case)
#     ind = case_ind[case.index(fin)]
#     return fin, ind
#
#
# for _ in range(t):
#     final = []
#     n, m = map(int, input().split())
#     result = [[0] * m for _ in range(n)]
#     mapp = list(map(int, input().split()))
#     k = -1
#     for i in range(n):
#         for j in range(m):
#             k += 1
#             result[i][j] = mapp[k]
#     fin = 0
#     ind = 0
#     for i in range(n):
#         if result[i][0] > fin:
#             fin = result[i][0]
#             ind = (i, 0)
#     final.append(fin)
#     for _ in range(m-1):
#         fin, ind = find_next(result, ind)
#         final.append(fin)
#
#     print(sum(final))

############ Question 2 ########################################################################

## 답 ##
# n = int(input())
# dp = []
#
# for _ in range(n):
#     dp.append(list(map(int, input().split())))
#
# for i in range(1, n):
#     for j in range(i+1):
#         if j == 0:
#             up_left = 0
#         else:
#             up_left = dp[i-1][j-1]
#         if j == i:
#             up = 0
#         else:
#             up = dp[i-1][j]
#         dp[i][j] = dp[i][j] + max(up_left, up)
#
# print(max(dp[n-1]))

######### Question 3 #######################################################################
#
# n = int(input())
# lis = []
# lis.append(0)
# temp = [0] * (n + 1)
# for i in range(n):
#     t, p = map(int, input().split())
#     lis.append((t, p))
#
# for i in range(1, n+1):
#     if i + (lis[i][0]-1) < len(lis):
#         temp[i + (lis[i][0]-1)] = max(lis[i][1] + temp[i-1], temp[i + (lis[i][0]-1)])
# print(max(temp))

########### Question 4 #################################################################
# n = int(input())
# attack = list(map(int, input().split()))
# temp = []
# min_val = int(1e9)
# minu = 0
# for i in range(n):
#     if attack[i] < min_val:
#         min_val = attack[i]
#         temp.append(attack[i])
#     else:
#         minu += 1
#         temp.remove(min_val)
#         temp.append(attack[i])
#         min_val = min(temp)
#
# print(minu)

######### Question 5 #################################################################
# 1, (2,3,5)를 약수로 가지는 수는 못생긴 수
# n = int(input())
# c = 1
# i = 2
# while c != n:
#     if i%2 == 0 or i%3 == 0 or i%5 == 0:
#         c += 1
#     i += 1
#
# print(i-1)

########## Question 6 ###########################################################
# A를 삽입, 삭제, 교체를 하여 B로 만든다. 최소 편집수를 계산하라!
# 1. 길이가 다르다 => 삭제 or 삽입, 2. 1에서 끝나던가 교체

w1 = list(input())
w2 = list(input())
w1_len = len(w1)
w2_len = len(w2)
c = 0
j = 0
for i in range(max(w1_len, w2_len) if w2_len > w1_len else min(w1_len, w2_len)):
    if len(w1) != len(w2):
        if w1[i] != w2[i] and len(w1) < len(w2):
            w1.insert(i, w2[i])
            c += 1
        elif w1[i - j] != w2[i - j] and len(w1) > len(w2):
            w1.remove(w1[i-j])
            c += 1
            j += 1
    else:
        if w1[i-j] != w2[i-j]:
            w1[i-j] = w2[i-j]
            c += 1
print(c)

