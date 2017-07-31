"""
Print triangle, below example for n = 5
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1

"""

def triangle(n):
    if n < 0:
        return None
    elif n == 1:
        return 1

    res = [[1], [1, 1]]
    if n == 2:
        return res
    ap = [1, 1]
    anext = [1]
    print anext
    print ap
    for i in range (2, n):
        for j in range (1, i):
            anext.append(ap[j-1] + ap[j])
        anext.append(1)
        print anext
        res.append(anext)
        ap, anext = anext, [1]
    return res


triangle(10)

# Output:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
