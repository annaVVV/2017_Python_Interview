# Open a file, read line by line, print the number of lines, print the number of words.
#
# filename: Test.txt
# hello
# blue is my favourite color
# yellow is also my favourite color
#
#
# output:
# Number of lines: 3
# Number of words: 12
#
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

print 'Number of lines:', file_len("text.txt")
str = open("text.txt").read()
print 'Number of words:', len(str.split())

# One more:
lines, words = 0, 0
with open('text.txt') as file:
    for line in file:
        lines += 1
        words += len(line.split())
print lines, words  
# Output: 3, 12

