def count_check(x, arra):
    result = 0
    for j, k in enumerate(arra):
        check = 1
        for q in range(len(k) - 1):
            if k[q] != k[q+1]:
                check += 1
        if check <= x[j]:
            result += 1
    return result


a = input()
a = int(a)
arr = [list(input()) for i in range(a)]
count = []
for i, v in enumerate(arr):
    length = len(set(v))
    count.append(length)

print(count_check(count, arr))
