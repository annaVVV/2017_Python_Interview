import re

str = 'an example word:cat!!'
match = re.search(r'word:\w\w\w', str)
# If-statement after search() tests if it succeeded
if match:
    print 'found', match.group() ## 'found word:cat'
else:
    print 'did not find'

str = 'purple.alice-b@google.com monkey dishwasher'
match = re.search(r'\w+@\w+', str)
if match:
    print match.group()  ## 'b@google'
    
"""
Square Brackets
Square brackets can be used to indicate a set of chars, so [abc]
matches 'a' or 'b' or 'c'. The codes \w, \s etc.
work inside square brackets too with the one exception that dot (.)
just means a literal dot. For the emails problem,
the square brackets are an easy way to add '.' and '-' to the set
of chars which can appear around the @ with the pattern
r'[\w.-]+@[\w.-]+' to get the whole email address
"""

match = re.search(r'[\w.-]+@[\w.-]+', str)
if match:
    print match.group()  ## 'alice-b@google.com'

str = 'purple alice-b@google.com monkey dishwasher'
match = re.search('([\w.-]+)@([\w.-]+)', str)
if match:
    print match.group()   ## 'alice-b@google.com' (the whole match)
    print match.group(1)  ## 'alice-b' (the username, group 1)
    print match.group(2)  ## 'google.com' (the host, group 2)
