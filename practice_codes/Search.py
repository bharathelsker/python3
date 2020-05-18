pos = -1


def search(list, n):
    l = 0
    u = len(list) - 1
    while l <= u:
        mid = (l + u) // 2
        if list[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < n:
                l = mid
            else:
                u = mid
    return False


list1 = [9, 1, 5, 2, 3, 7, 4, 8, 5, 6, 3]
list = list(dict.fromkeys(list1))
list.sort()

n = 9

if search(list, n):
    print('Found at', pos + 1)
else:
    print('Not found')
