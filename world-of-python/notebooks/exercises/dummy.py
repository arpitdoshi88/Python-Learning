import string

def print_rangoli(size):
    """
    Print a rangoli pattern of lowercase English letters.
    Parameters
    ----------
    size : int
        Number of letters to use in the rangoli. The pattern will use letters from 'a' up to the
        letter at position `size` in the alphabet (1 -> 'a', 2 -> 'b', ...). Must be a positive integer.
    Returns
    -------
    None
        The function prints the rangoli directly to standard output (stdout). It does not return a value.
    Behavior
    --------
    The rangoli is a symmetric, diamond-like pattern where each row contains letters separated by
    hyphens ('-') and padded with hyphens to a fixed width so that rows are centered. The middle (widest)
    row contains the sequence of letters from the `size`-th letter down to 'a' and back up to the
    `size`-th letter, e.g. for size=3 the middle row is "c-b-a-b-c". The full pattern has (2*size - 1)
    rows: the top half (size-1 rows), the middle row, and the bottom half which mirrors the top.
    Raises
    ------
    TypeError
        If `size` is not an integer.
    ValueError
        If `size` is less than 1.
    Examples
    --------
    >>> print_rangoli(1)
    a
    >>> print_rangoli(3)
    ----c----
    --c-b-c--
    c-b-a-b-c
    """
    
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