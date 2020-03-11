"""
  Write a Python program to print the following string in a specific format (see the output).
  Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the 
    world so high, Like a diamond in the sky. Twinkle, twinkle, little star, 
    How I wonder what you are" 
    
    Output:

  Twinkle, twinkle, little star,
    How I wonder what you are! 
      Up above the world so high,   		
      Like a diamond in the sky. 
  Twinkle, twinkle, little star, 
    How I wonder what you are
"""

string = 'Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are'
string_list = string.split(' ')
commas = 0
new_string = ''

for word in string_list:
    if '!' in word:
        new_string += word + ' '
        new_string += '\n\t\t'
    elif '.' in word:
        new_string += (word.strip().strip()) + ' \n'
        commas = 0
    elif ',' in word:
        commas += 1
        new_string += word + ' '
        if commas == 3:
            new_string += '\n\t'
            # new_string += word + ' '
        elif commas > 3:
            new_string += '\n\t\t'

    # elif commas >= 3:
    #   pass
    else:
        new_string += word + ' '
print(f'{new_string}')
