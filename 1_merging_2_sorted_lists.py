'''
Merging two sorted list
We have two sorted lists, and we want to write a function to merge the two lists into one sorted list:
a = [3, 4, 6, 10, 11, 18]
b = [1, 5, 7, 12, 13, 19, 21]
'''

def merge(a,b):
    len_a = len(a)
    len_b = len(b)
    a_b = []
    j = 0
    i = 0
    while True:
        if (a[i]<b[j]):
            a_b.append(a[i])
            i += 1
            if i == len(a):
                a_b.extend(b[j:])
                break
        else:
            a_b.append(b[j])
            j += 1
            if j == len_b:
                a_b.extend(a[i:])
                break
    return a_b

a = [3, 4, 6, 10, 11, 18]
b = [1, 5, 7, 12, 13, 19, 21]


a_b = merge(a,b)
print (a_b)

def merge1(a,b):
    a.extend(b)
    c = sorted(a)
    print(c)
    return c


def merge3(a,b):
    c = []

    while a and b:
        if a[0] < b[0]:
            c.append(a.pop(0))
        else:
            c.append(b.pop(0))

    # either a or b can be not empty
    print (c + a + b)
    return c + a + b

'''
Expected result:
[1, 3, 4, 5, 6, 7, 10, 11, 12, 13, 18, 19, 21]
'''
