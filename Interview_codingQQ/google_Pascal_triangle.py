"""
Write a function which implements the Pascal's triangle:

1
1    1
1    2    1
1    3    3    1
1    4    6    4    1
1    5    10    10    5    1
"""

def paskal0(n):
    if n==0: return []
    prev_line = paskal(n-1)
    line = [1]
    for i in range(len(prev_line)-1):
        line.append(prev_line[i] + prev_line[i+1])
    line += [1]
    return line

def paskal(n):
    if n==0: return []
    p_line = paskal(n-1)
    line = [p_line[i] + p_line[i+1] for i in range(len(p_line)-1)]
    line.insert(0,1)
    line.append(1)
    return line

for i in range(10):
    print paskal(i)
