def any_two_sum(numbers, total):
    '''This function takes to inputs and outputs True if any two integers in numbers sum to total and False otherwise'''
    two_sum = set() # Empty Set
    
    for i in numbers: # Interating through numbers
        one_sum = total - i # Creating new variable which stores the total - the index
        if one_sum in two_sum: # If number is already in the empty set it adds up too total
            return True
        two_sum.add(i) # Adding number in set to store
    
    return False

