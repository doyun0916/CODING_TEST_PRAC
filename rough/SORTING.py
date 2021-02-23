# ## Q23 ##
# n = int(input())
# candi = []
# for i in range(n):
#     candi.append(list(input().split()))
# candi.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
# for c in candi:
#     print(c[0])

# ## Q24 ##
# n = int(input())
# houses = list((map(int, input().split())))
# houses.sort()
# print(houses[(n-1)//2])

## Q25 ##
# def solution(N, stages):
#     result = []
#     final = [0] * N
#     player = len(stages)
#     for i in range(1, N+1):
#         loser = stages.count(i)
#         temp = loser/player
#         result.append((temp, i))
#         player -= loser
#     result.sort(key=lambda x: (x[0], -x[1]))
#     result.reverse()
#     for j in range(len(result)):
#         final[j] = result[j][1]
#     answer = final
#     return answer

## Q26 ##
n = int(input())
nums = []
for i in range(n):
    nums.append(int(input()))
nums.sort()
before = nums[0]
result = 0
for i in range(1, len(nums)):
    result = result + before + nums[i]
    before = result
print(result)
# 답:
import heapq
n = int(input())
heap = []
for i in range(n):
    heapq.heappush(heap, int(input()))
result = 0
while len(heap) != 1:
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)
    sum_value = one + two
    result += sum_value
    heapq.heappush(heap, sum_value)
print(result)