# 1
n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
arr.sort()
arr.reverse()
for i in range(len(arr)):
    print(arr[i], end=' ')

# 2
n = int(input())
arr=[]
for _ in range(n):
    temp = list(input().split())
    arr.append((temp[0], int(temp[1])))

def setting(data):
    return data[1]

result = sorted(arr, key=setting)
for i in range(len(result)):
    print(result[i][0], end=' ')

# 3
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = 0
while c != k:
    if min(a) < max(b):
        a[a.index(min(a))], b[b.index(max(b))] = b[b.index(max(b))], a[a.index(min(a))]
        c += 1
    else:
        break
print(sum(a))