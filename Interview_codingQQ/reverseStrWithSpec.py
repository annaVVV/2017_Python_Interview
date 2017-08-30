"""
Reverse a string, special characters should retain on the same index
 Input:  "adf$gydpjmw&v xt"
 Output: "txv$wmjpdyg&f da"
"""

str = 'adf$gydpjmw&v xt'
print 'Input: ', str
l = list(str)
i,j = 0, len(l)-1
while i<j:
    if not l[i].isalnum():
        i += 1
    elif not l[j].isalnum():
        j -= 1
    else:
        l[i], l[j] = l[j], l[i]
        i += 1
        j -= 1

print 'Output:', ''.join(l)
