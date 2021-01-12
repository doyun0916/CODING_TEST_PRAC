def switch(x):
    return {'-': 0, '\\': 1, '(': 2, '@': 3, '?': 4, '>': 5, '&': 6, '%': 7, '/': -1}.get(x, "default")


nums = []
a = input()
nums.append(a)
while a != '#':
    a = input()
    if a == '#':
        break
    else:
        nums.append(a)

for i, v in enumerate(nums):
    power = len(v) - 1
    result = 0
    for j in v:
        temp = switch(j)
        temp2 = (8 ** power) * temp
        result += int(temp2)
        power -= 1
    nums[i] = result
for i in nums:
    print(i)
