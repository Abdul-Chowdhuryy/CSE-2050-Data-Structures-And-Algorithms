
def ways_to_sum_memo(n, total):
    '''This function determines how many different ways one could repeatedly sum die rolls and
        get to a given total through the recursive method of memoization'''
    memoization = {}
    sides = n
    if sides <= 0 or total <= 1:
        return 0
    if sides == 1:
        return 1
    
    if (n, total) in memoization:
        return memoization([n, total])
    
    counter = 0
    for i in range(1, sides+1):
        if total - i >= 0:
            counter += ways_to_sum_memo(n, total - i)
    
    memoization([n, total]) == counter
    return counter

def ways_to_sum_tab(n, total):
    '''This function determines how many different ways one could repeatedly sum die rolls and
        get to a given total through the iterative method of tabulation'''
    sides = n
    if sides <= 0 or total <= 1:
        return 0
    if sides == 1:
        return 1
    table = [0] * (total + 1)
    table[0] = 1

    for i in range(1, total+1):
        for y in range(1, sides+1):
            if i - y >= 0:
                table[i] += table[i-y]
    return table[total]

