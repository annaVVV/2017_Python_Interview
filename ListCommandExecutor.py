"""
Imput:
a number of commands to be executed (n)
n lines with commands to interracr with a list 
"""

# Data example

"""
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
"""
n = raw_input()
L = []
commands = []
for i in range(0,int(n)):
    singleComm = []
    singleComm = raw_input().split()
    commands.append(singleComm)

for elem in commands:
    if elem[0] == 'insert':
        L.insert(int(elem[1]), int(elem[2]))
    elif elem[0] == 'print':
        print L
    elif elem[0] == 'remove':
        L.remove(int(elem[1]))
    elif elem[0] == 'append':
        L.append(int(elem[1]))
    elif elem[0] == 'sort':
        L.sort()
    elif elem[0] == 'reverse':
        L.reverse()
    elif elem[0] == 'pop':
        L.pop()
        
        
# Output:

# [6, 5, 10]
# [1, 5, 9, 10]
# [9, 5, 1] 
