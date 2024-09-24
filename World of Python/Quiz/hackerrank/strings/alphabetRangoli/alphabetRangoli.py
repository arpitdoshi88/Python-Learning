#You are given an integer, . Your task is to print an alphabet rangoli of size . (Rangoli is a form of Indian folk art based on creation of patterns.)

# Different sizes of alphabet rangoli are shown below:

# The center of the rangoli has the first alphabet letter a, and the boundary has the  alphabet letter (in alphabetical order).

# Function Description

# Complete the rangoli function in the editor below.

# rangoli has the following parameters:

# int size: the size of the rangoli
# Returns

# string: a single string made up of each of the lines of the rangoli separated by a newline character (\n)
# Input Format

# Only one line of input containing , the size of the rangoli.

import string

def print_rangoli(size):
    if(size > 0 and size < 27 ):
        alphabets = list(string.ascii_lowercase)
        alphas = list(alphabets[:size])
        reversedAlphas =  list(reversed(alphas)) # or list(alphas[::-1]) 
        width = (size-1)*4 + 1 

        middle_line = "-".join(reversedAlphas[:-1] + alphas)

        upper_half = []
        for i in range(1,size):
            upper_half.append("-".join(reversedAlphas[:-1*size+i-1]+ alphas[-1*i:]).center(width,"-")) 
        lower_half = list(reversed(upper_half))
        
        print("\n".join(upper_half + [middle_line] +lower_half))
    else:
        print("size must be <=26")

    
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)