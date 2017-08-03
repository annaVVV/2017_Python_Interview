grid = [ [ 'A','F','H','D','T','K','P','E','P','G'],
         [ 'J','G','R','E','E','N','T','P','W','R'],
         [ 'U','R','G','E','P','Q','Y','K','W','E'],
         [ 'P','Q','R','A','C','R','T','P','W','E'] ]

#input -- "GREEN"

#expected output -- (1,1)


def search_word(grid, word):
    lw = list(word)
    l1 = len(grid)
    ii = 0
    for i in range(l1):
        str = ''.join(grid[i])
        ind = str.find(word)
        if ind > -1:
            return (i, ind)
    return None

word = "GREEN"
print search_word(grid, word)
