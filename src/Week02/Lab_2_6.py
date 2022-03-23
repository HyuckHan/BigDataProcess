def max(*ints):
    m = -1 
    for n in ints:
        if m < n:
            m = n
    return m

print(max(1, 4, 6))
print(max(10, 5, 87, 57, 38))
print(max(4, 3, 2, 1))
