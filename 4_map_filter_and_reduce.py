# Using map, filter, reduce, write a code that create a list of (n)**2 for range(10) for even integers:

l = [x for x in range(10) if x % 2 == 0]
print (l)

m = filter(lambda x:x % 2 == 0, [x for x in range(10)] )
print (m)

o = map(lambda x: x**2, m)
print (o)

from functools import reduce
p = reduce(lambda x,y:x+y, o)
print (p)

# Output:
#
# [0, 2, 4, 6, 8]
# [0, 2, 4, 6, 8]
# [0, 4, 16, 36, 64]
# 120
