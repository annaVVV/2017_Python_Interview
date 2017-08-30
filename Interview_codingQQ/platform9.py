"""
Given table (grid) with letters and a string (word)
If the string found in any row of the table as a sequence, return  (row, column) or nothing if not found
#input -- "GREEN"
#expected output -- (1,1)
"""

def search_word(grid, word):
    # Search each row
    for i in range(len(grid)):
        str = ''.join(grid[i])
        ind = str.find(word)
        if ind > -1:
            return (i, ind)
    return None


# Given table with letters
grid = [ [ 'A','F','H','D','T','K','P','E','P','G'],
         [ 'J','G','R','E','E','N','T','P','W','R'],
         [ 'U','R','G','E','P','Q','Y','K','W','E'],
         [ 'P','Q','R','A','C','R','T','P','W','E'] ]

# String to lookup
word = "GREEN"
print search_word(grid, word)
