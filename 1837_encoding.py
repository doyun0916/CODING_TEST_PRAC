def isotest(x):
    for i in range(2, x):
        if x % i == 0:
            return 0
    return x


p, k = input().split()
p = int(p)
k = int(k)
check1 = 1
adv = []
while p//2 != check1:
    a = p//check1
    b = p % check1
    if b == 0:
        a_new = isotest(a)
        b_new = isotest(check1)
        if a_new != 0 and b_new != 0:
            adv.append([a_new, b_new])
    check1 += 1
    if check1 > a:
        break
if adv[0][0] > k and adv[0][1] > k:
    print('GOOD')
else:
    if (adv[0][0] > adv[0][1]) is True:
        print('BAD' + ' ' + str(adv[0][1]))
    else:
        print('BAD' + ' ' + str(adv[0][0]))