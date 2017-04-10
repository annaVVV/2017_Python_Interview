'''
Get word frequency - initializing dictionary
'''
ss = """I figured it out
I figured it out from black and white
Seconds and hours
Maybe they had to take some time"""

# Initialize the dictionary with 0 using fromkeys()
words = ss.split()
d = {}.fromkeys(words,0)
for w in words:
    d[w] += 1
print (d)

# Here is another way of initializing a dictionary:

d = {}
for w in ss.split():
    d[w] = d.get(w,0) + 1
print (d)

'''
 output should look like this:

{'I': 2, 'figured': 2, 'Maybe': 1, 'white': 1, 'Seconds': 1, 'it': 2, 'time': 1, 'hours': 1, 'some': 1, 'out': 2, 
'had': 1, 'they': 1, 'and': 2, 'from': 1, 'take': 1, 'to': 1, 'black': 1}

'''
