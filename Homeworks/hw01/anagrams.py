def  is_anagram(word1, word2):
   '''This function checks if two words are anagrams meaning it checks whether two different words have
   identical letters and length'''
   sorted_word1 = sorted(word1)# Sorting the strings from a-z using python built in function
   sorted_word2 = sorted(word2)
   if len(sorted_word1) != len(sorted_word2): # If statement making sure length of both words are the same
      return False
   elif sorted_word1 == sorted_word2: # If statement checking if sorted words have equal letters therefore anagram
      return True
   else: # else statement accounts for everything else
      return False






