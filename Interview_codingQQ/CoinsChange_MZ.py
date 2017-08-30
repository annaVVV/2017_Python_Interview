# https://www.youtube.com/watch?v=3VBjhiKUtmE
"""
Print all possible combinations of coins [1, 2, 5] per change amount 5
Solution:
1. Sort coins from large to small based on amount
2. Determine how many large coins used
3. Calculate how much the amount left using a given number of large coins
4. Recursion to the deducted value using sub-set of the coins
5. Print out of the remaining amount dividable by the smallest coin amount
"""
res = []
def change(amount, coins, counts, i):
    # Should we proceed?
    if i >= len(coins): # we used all coins
        # Add a new combination
        res.append({x:y for x,y in zip(coins,counts)})
        return
    # otherwise we need to proceed
    # if index i is the last coin, check in amount left is combination of the smallest coin
    if i == len(coins)-1:
        if amount%coins[i] == 0: # good combination
            counts[i]=amount/coins[i]
            change(0, coins, counts, i+1)
    else:
        for j in range(amount/coins[i]+1):
            counts[i] = j
            # recursive call with amount left
            change(amount-j*coins[i], coins, counts, i+1)

print 'Solution:'
change(cents, [5, 2, 1], [0,0,0], 0)
print res

# Solution:
# [{1: 5, 2: 0, 5: 0}, {1: 3, 2: 1, 5: 0}, {1: 1, 2: 2, 5: 0}, {1: 0, 2: 0, 5: 1}]
