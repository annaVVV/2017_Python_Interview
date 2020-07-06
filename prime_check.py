def fibo_gen(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b

for i in fibo_gen(5):
    print(i, end = ' ')

# Result
###
29 5
29 is a prime number
True
169 13
169 could be devided by 13
False
###
