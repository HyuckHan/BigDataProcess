for i in range(0, 10):
    for j in range(0, 10):
        if j < 10 - i - 1:
            print(' ', end = '')
        else:
            print('*', end = '')
    print('')
