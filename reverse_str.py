def rev_str(s1):
    l = len(s1)
    if l < 2:
        return s1
    i = 0
    j = l - 1
    s = list(s1)
    while i < j:
        print( s[i], s[j])
        s[i], s[j] = s[j], s[i]
        i = i + 1
        j = j - 1
    return ''.join(s)

def reverse(s):
  str = ""
  for i in s:
    str = i + str
  return str

# Python code to reverse a string
# using recursion

def reverse1(s):
    if len(s) == 0:
        return s
    else:
        return reverse1(s[1:]) + s[0]

if __name__ == '__main__':
    print(rev_str('asdfgh'))
    s = "Geeksforgeeks"

    print("The original string  is : ", end="")
    print(s)

    print("The reversed string(using recursion) is : ", end="")
    print(reverse1(s))
