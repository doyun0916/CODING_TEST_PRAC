## Q31 ##
# t = int(input())
# for _ in range(t):
#     n, m = map(int, input().split())
#     mapp = [[0] * (m) for _ in range(n)]
#     nums = list(map(int, input().split()))
#     k = -1
#     for i in range(n):
#         for j in range(m):
#             k += 1
#             mapp[i][j] = nums[k]
#
#     current = ()
#     cum = int(-1e9)
#     for p in range(n):
#         if cum < mapp[p][0]:
#             current = (p, 0)
#             cum = mapp[p][0]
#
#     movement_x = [-1, 0, 1]
#     movement_y = [1, 1, 1]
#     for q in range(m-1):
#         maxi = int(-1e9)
#         current_new = ()
#         for g in range(3):
#             dx = movement_x[g] + current[0]
#             dy = movement_y[g] + current[1]
#             if 0 <= dx < n and 0 <= dy < m:
#                 if maxi < mapp[dx][dy]:
#                     current_new = (dx, dy)
#                     maxi = mapp[dx][dy]
#         cum += maxi
#         current = current_new
#
#     print(cum)

## Q32 ##
# n = int(input())
# mapp = [[0] * n for _ in range(n)]
# mapp_result = [[0] * n for _ in range(n)]
# for i in range(n):
#     temp = list(map(int, input().split()))
#     for j in range(len(temp)):
#         mapp[i][j] = temp[j]
#
# movement_x = [1, 1]
# movement_y = [0, 1]
# maxi = int(-1e9)
# mapp_result[0][0] = mapp[0][0]
# for i in range(n-1):
#     for j in range(n-1):
#         for k in range(2):
#             dx = i + movement_x[k]
#             dy = j + movement_y[k]
#             if 0 <= dx < n and 0 <= dy < n:
#                 temp = mapp_result[i][j] + mapp[dx][dy]
#                 mapp_result[dx][dy] = max(mapp_result[dx][dy], temp)
#
# print(max(mapp_result[n-1]))

## Q33 ##
# n = int(input())
# t = [0]
# p = [0]
# for i in range(n):
#     time, pay = map(int, input().split())
#     t.append(time)
#     p.append(pay)
#
# final = []
# for k in range(1, n+1):
#     p_result = [0] * (n + 1)
#     length = n
#     cur_index = k
#     while True:
#         target_index = (cur_index - 1) + t[cur_index]
#         if target_index > n:
#             break
#         val = p[cur_index] + p_result[target_index - 1]
#         for i in range(target_index, n+1):
#             p_result[i] = val
#         cur_index = target_index + 1
#         if cur_index > n:
#             break
#     final.append(max(p_result))
#
# print(max(final))

# ## Q34 ##
# n = int(input())
# sol = list(map(int, input().split()))
# sol.reverse()
# dp = [1] * n
# cur = sol[0]
# cur_index = 0
# for i in range(1, n):
#     if sol[i] > cur:
#         dp[i] += dp[cur_index]
#         cur = sol[i]
#         cur_index = i
#
# print(n - max(dp))

## Q35 ##
n = int(input())
dp = [1]
maximium = int(1e9)
for i in range(2, maximium):
    if i%2 == 0 or i%3 == 0 or i%5 == 0:
        dp.append(i)
        if len(dp) == n:
            break

print(dp[-1])

## Q36 ##
#???