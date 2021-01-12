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
# # 한줄씩 입력 받기
# import sys
# input_data = sys.stdin.readline().rstrip()
# print(input_data)

n, m = map(int, input().split())
arr = list(map(int, input().split()))
result = []
temp = []
for i in range(max(arr)):
    for j in range(len(arr)):
        if arr[j] < i+1:
            continue
        else:
            temp.append(arr[j]-i-1)
    result.append(sum(temp))
    temp = []
for k in range(len(result)):
    if result[k] <= m:
        print(k+1)
        break

