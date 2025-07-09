def remove_characters(input_string, to_remove):
    '''This functions takes two inputs and returns a string 
    that is exactly the same as the input_string but without any of the characters in to_remove.'''
    new_string = '' # Empty String
    for i in input_string: # Iterating through input_string
        if i not in to_remove: # If the index does not find the letter in to_remove
            new_string += i # Add it to empty string
    return new_string
    

