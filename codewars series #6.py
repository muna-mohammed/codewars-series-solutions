# the link:
# https://www.codewars.com/kata/595970246c9b8fa0a8000086/train/python

# the question is : 
# Capitalization and Mutability

'''
instractions:
Your coworker was supposed to write a simple helper function to capitalize a string (that contains a single word) before they went on vacation.

Unfortunately, they have now left and the code they gave you doesn't work. Fix the helper function they wrote so that it works as intended (i.e. make the first character in the string "word" upper case).

Don't worry about numbers, special characters, or non-string types being passed to the function. The string lengths will be from 1 character up to 10 characters, but will never be empty.

'''
# question:
def capitalize_word(word):
    return "".join(char.upper() for char in word)
    
# my own solution:
def capitalize_word(word):
    
    return word[0].upper() + word[1:]

# we will just take the parameter from the line no.1 and will pass it in line no.2 ,,in line 2 if we use char like before in the question 
#it will say that tha char is not defines , and if we try to add it in the pararmeter in line 1  it will say one argument is missing from capitaliz_word function
    
 
 
# onther solution
def capitalizeWord(word):
    return word.capitalize()
  
  # other solution:
  def capitalizeWord(word):
    return word.tital()
