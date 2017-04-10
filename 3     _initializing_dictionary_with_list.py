'''
Initializing dictionary with list
Sometimes we may want to construct dictionary whose values are lists.

In the following example, we make a dictionary like {'Country': [cities,...], }:
'''

cities = {'San Francisco': 'US', 'London':'UK',
        'Manchester':'UK', 'Paris':'France',
        'Los Angeles':'US', 'Seoul':'Korea'}

# => {'US':['San Francisco', 'Los Angeles'], 'UK':[,], ...}

from collections import defaultdict
# using collections.defaultdict()
d1 = defaultdict(list) # initialize dict with list
for k,v in cities.items():
    d1[v].append(k)
print (d1)

# using dict.setdefault(key, default=None)
d2 = {}
for k,v in cities.items():
       d2.setdefault(v,[]).append(k)
print (d2)

# Output:
#
# defaultdict(<class 'list'>, {'France': ['Paris'], 'US': ['Los Angeles', 'San Francisco'], 'UK': ['London', 'Manchester'], 'Korea': ['Seoul']})
# {'France': ['Paris'], 'US': ['Los Angeles', 'San Francisco'], 'UK': ['London', 'Manchester'], 'Korea': ['Seoul']}
