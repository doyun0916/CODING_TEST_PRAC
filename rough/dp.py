# x = int(input())
#
# d = [0] * 30001
#
# for i in range(2, x+1):
#     d[i] = d[i-1] + 1
#     if i%2 == 0:
#         d[i] = min(d[i], d[i//2]+1)   # 그
#     if i % 3 == 0:
#         d[i] = min(d[i], d[i // 3] + 1)
#     if i%5 == 0:
#         d[i] = min(d[i], d[i//5]+1)
#
# print(d[i])
#
# # i 는 아래숫자부터 차례로, 26까지 어떤식으로 쌓아가야 도달하는가를 측정하기 위한 경우의 수
# # d 는 그저 그 숫자까지 몇번이 필요한가를 판별하는 것!
# # 나눈 몫의 수 까지 도달하는데 걸린 횟수 + 1 해서 그 나눴을때의 숫자라고 하는 것!
#
# n = int(input())
# array = list(map(int, input().split()))
# d = [0] * 100
#
# d[0] = array[0]
# d[1] = max(array[0], array[1])
# for i in range(2, n):
#     d[i] = max(d[i-1], d[i-2] + array[i])
#
# print(d[n-1])
#
#
# ##################
# n = int(input())
# d = [0] * 1001
# for i in range(3, n+1):
#     d[i] = (d[i-1] + 2 * d[i-2]) % 796796
#
# print(d[i])
#
# # 1로 쭉 가다가, 2개로 나눠질때는, 전전으로 돌아가서 *2로 분열해줌!
#
#
# n 종류 화폐
# 화폐 개수 최소한 -> 합이 m이 되도록.
# 화폐 개수 제한 x,

n, m = map(int, input().split())
mon =[]
for i in range(n):
    mon.append(int(input()))

arr = [10001] * (m+1)
arr[0] = 0
for j in range(n):
    t = mon[j]
    for i in range(t, m+1, t):
        if i%t == 0:
            arr[i] = min(arr[i-t] + 1, arr[i])

if arr[m] == -1:
    print(-1)
else:
    print(arr[m])
