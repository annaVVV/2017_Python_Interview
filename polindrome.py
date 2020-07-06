def is_polinddrome(s):
    s = s.lower()
    rev = reversed(s)
    return list(rev) == list(s)

print(is_polinddrome('qwer'))
print(is_polinddrome('abnba'))
