# Get prima number from 1 to 100

def primes(n=1):
   while n < 100:
      # yields n instead of returns n
      if isPrime(n): yield n
      # next call it will increment n by 1
      n += 1

def isPrime(n):
   if n == 1:
      return False
   for t in range(2,n):
      if n % t == 0:
         return False
   return True

print 'Prime numbers:'
for n in primes():
   print n,
print


def isP(n):
    if n == 1:
        return False
    for t in range(2,n):
        if n%t ==0:
            return False
    return True

print 'Test  Prime numbers:'
print [n for n in range(1, 101) if isP(n)]

# Output:
# Prime numbers:
# 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97
# Test  Prime numbers:
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
