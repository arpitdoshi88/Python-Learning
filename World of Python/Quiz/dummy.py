import string

def print_rangoli(size):
    alphabates = string.ascii_lowercase
    reversedAlphabets = list(reversed(alphabates[:size]))
    width = (size-1) * 4 + 1 
    # your code goes here
    middle_line = "-".join((reversedAlphabets[:-1]+reversedAlphabets[::-1]))
    top_layer,bottom_layer = [],[]
    for i in range(1,size):
        top_layer.append("-".join(reversedAlphabets[:-1*size+i-1] + reversedAlphabets[::-1][-1*i:]).center(width, "-"))
    
    print("\n".join(top_layer),middle_line,"\n".join(reversed(top_layer)),sep='\n')

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)