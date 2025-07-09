###############################################################################
# Collaboration                                                               #
# -------------                                                               #
# You can collaborate with up to 3 classmates (for a total of 4 students per  #
# group). If you do so, remember not to share code directly. Discussions are  #
# fine, code sharing is not. Also note that all have to submit individually.  #
#                                                                             #
# Enter any collaborators here:                                               #
# Collaborator 1:                                                             #
# Collaborator 2:                                                             #
# Collaborator 3:                                                             #
###############################################################################
  
def fizzbuzz(start, finish):
    '''This program checks whether a number is a multiple of 3 (outputting fizz), 5 (outputting buzz), or both (outputting fizzbuzz). I later converted the index to a string to check a few more cases, such as if it contains a 5 and is a multiple of 3 (vice versa as well), and also if it contains either a 5 or 3, it would output its respective output.'''

    for i in range(start, finish + 1):
       
        str_i = str(i) # converting to string to check if 3 or 5 is in code

        if i % 3 == 0 and i % 5 == 0: # both multiple of 3 and 5
            print("fizzbuzz")
        elif '3' in str_i and '5' in str_i: # 3 and 5 in number using str i
                print("fizzbuzz")
        elif i % 3 == 0 and '5' in str_i: # multiple of 3 using regular i and 5 in number using str i 
                print("fizzbuzz")
        elif i % 5 == 0 and '3' in str_i: # multiple of 5 using regular i and 3 in number using str i
                print("fizzbuzz")
        elif '3' in str_i: # if 3 in number using string i
             print("fizz")
        elif '5' in str_i: # if 5 is in number using string i
             print("buzz")
        elif i % 3 == 0: # multiple of 3
            print("fizz")
        elif i % 5 == 0: # multiple of 5
            print("buzz")
        else: # all other cases
         print(i)
    pass

  
  







