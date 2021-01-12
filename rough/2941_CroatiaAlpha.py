def equal(a, length, count):
    if a[length] == '=':
        length -= 1
        if (a[length] == 'c') or (a[length] == 's'):
            count += 1
            length -= 1
            return count, length
        elif a[length] == 'z':
            length -= 1
            if a[length] == 'd':
                length -= 1
                count += 1
                return count, length
            else:
                count += 1
                return count, length
        else:
            count += 1
    return count, length

def minus(a, length, count):
    if a[length] == '-':
        length -= 1
        if (a[length] == 'c') or (a[length] == 'd'):
            length -= 1
            count += 1
        else:
            count += 1
    return count, length

def jay(a, length, count):
    if a[length] == 'j':
        length -= 1
        if (a[length] == 'l') or (a[length] == 'n'):
            length -= 1
            count += 1
        else:
            count += 1
    return count, length


a = list(input())
length = len(a) - 1
count = 0
while 1:
    if (a[length] == '=') or (a[length] == '-') or (a[length] == 'j'):
        count, length = equal(a, length, count)
        count, length = minus(a, length, count)
        count, length = jay(a, length, count)
    else:
        length -= 1
        count += 1
    if length == -1:
        break
print(count)
