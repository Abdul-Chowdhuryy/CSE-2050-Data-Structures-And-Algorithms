
def contains_permutation(input_string, pattern):
    '''This program takes two inputs and returns true if input_string contains a sub string of pattern, and returns
    false if otherwise'''
    pattern_length = len(pattern) 
    pattern_frequency = dict() # Empty Dict to store values
    for i in pattern: # Frequency of characters in pattern
        pattern_frequency[i] = pattern_frequency.get(i, 0) + 1 
    # Iteration through input_string
    for i in range(len(input_string) - pattern_length + 1):
        substring = input_string[i:i + pattern_length]
        substring_freqency = dict()
        # Frequency of substring
        for i in substring:
            substring_freqency[i] = substring_freqency.get(i, 0) + 1
            # Checking if frequncy match 
        if substring_freqency == pattern_frequency:
            return True
        

    return False
    pass