a = input()
a = int(a)
nums = []
if not (1 <= a <= 1000000):
    exit()
for i in range(a):
    temp = input()
    temp = int(temp)
    if not (abs(temp) <= 1000000):
        exit()
    nums.append(temp)
nums.sort()
for j in nums:
    print(j)
