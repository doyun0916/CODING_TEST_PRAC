## Q27 ##
# n, x = map(int, input().split())
# nums = list(map(int, input().split()))
# def binary_search(array, target, start, end):
#     if start > end:
#         return None
#     mid = (start + end) // 2
#     if array[mid] == target:
#         return mid
#     elif array[mid] > target:
#         return binary_search(array, target, start, mid - 1)
#     else:
#         return binary_search(array, target, mid + 1, end)
#
# temp = 0
# count = 0
# while temp is not None:
#     temp = binary_search(nums, x, 0, len(nums)-1)
#     if temp is not None:
#         nums.pop(temp)
#         count += 1
#
# if temp != 0:
#     print(count)
# else:
#     print(-1)

## Q28 ##
# n = int(input())
# nums = list(map(int, input().split()))
# def binary_search(array, target, start, end):
#     if start > end:
#         return None
#     mid = (start + end) // 2
#     if array[mid] == target:
#         return mid
#     elif array[mid] > target:
#         return binary_search(array, target, start, mid-1)
#     else:
#         return binary_search(array, target, mid+1, end)
#
# result = False
# temp = 0
# for i in range(n):
#     temp = binary_search(nums, i, 0, n-1)
#     if temp is not None:
#         if temp == nums[temp]:
#             result = True
#             break
#
# if result:
#     print(temp)
# else:
#     print(-1)

## Q29 ##
# n, c = map(int, input().split())
# houses = []
# for i in range(n):
#     houses.append(int(input()))
#
# houses.sort()
# c -= 2
# gong_start = houses[0]
# gong_end = houses[-1]
# minimum = int(1e9)
# while c != 0:
#     mid = n // 2
#     minimum = min(minimum, houses[mid] - gong_start)
#     c -= 1
#
# print(minimum)

## Q30 ##
# if 'frodo' > 'fro??':
#     print(1)
# else:
#     print(0)
# def binary_search(array, target, start, end):
#     if start > end:
#         return None
#     mid = (start + end) // 2
#     if array[mid] == target:
#         return mid
#     elif array[mid] > target:
#         return binary_search(array, target, start, mid-1)
#     else:
#         return binary_search(array, target, mid+1, end)
