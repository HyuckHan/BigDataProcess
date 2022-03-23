for i in range(0, 10):
    for j in range(0, 10 - i - 1):
        print(' ', end = '')
    for j in range(0, i * 2 + 1):
        print('*', end = '')
    for j in range(0, 10 - i - 1):
        print(' ', end = '')
    print('')

"""
k = 10
for i in range(0, 10):
    k -= 1
    for j in range(0, 10):
        if j < k:
            print(' ', end = '')
        else:
            print('*', end = '')
    for j in range(9, -1, -1):
        if j < k:
            print(' ', end = '')
        else:
            print('*', end = '')
    print('')
"""