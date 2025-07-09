import string
def count_letters(file):
    '''This function opens a file and outputs the letter count pairs, I learned the importing string
function to input .ascii_lowercase and also the different built in functions such as isalpha() is lower() to 
lowercase letters and make sure the letter is a letter'''
    # empty dictionary to store letter:count pairs
 
    letter_count = {}
    
   

    # Opening the file using with
    with open(file, 'r') as f:
        for line in f:
            # Iterating through each character in the file
            for i in line:
                # Checking if the character is a letter and is in lowercase
                if i.isalpha() and i.lower() in string.ascii_lowercase: # checking if there is letters and lowercasing the letters
                    if i.lower() in letter_count:
                        letter_count[i.lower()] += 1 # if word is already in file then += 1
                    else: 
                        letter_count[i.lower()] = 1 # first encounter with word setting letter_count to 1
        for letter, count in letter_count.items():
            print(f"{letter}: {count}")
    f.close()
    return letter_count





