dup_list = [1,2,3,4,4,4,5,1,2,7,8,8,10]
print "Dupl:", dup_list
ss = set(dup_list) 
print ss
unique_list = [ x for x in iter(ss) ]
# Python 3
# unique_list = list(set(dup_list))

# Output:
# Dupl: [1, 2, 3, 4, 4, 4, 5, 1, 2, 7, 8, 8, 10]
# set([1, 2, 3, 4, 5, 7, 8, 10])
# Unique: [1, 2, 3, 4, 5, 7, 8, 10]

# ====================================================================================================

# Given a string which contains only lowercase letters, remove duplicate letters so that every letter appear once
#
# Example:
# Given "bcabc"     Return "abc"
# Given "cbacdcbc"  Return "acdb"

str = "cbacdcbc"
list = list(str)
print list

print str, ''.join(set(list))
# Output:
# ['c', 'b', 'a', 'c', 'd', 'c', 'b', 'c']
# cbacdcbc acbd
