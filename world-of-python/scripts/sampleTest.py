# write python function to filter even numbers from a list
def filter_even_numbers(numbers):
    """
    Filters even numbers from a given list of integers.
    
    Parameters
    ----------
    numbers : list of int
        A list containing integer values.
        
    Returns
    -------
    list of int
        A list containing only the even integers from the input list.
        
    Examples
    --------
    >>> filter_even_numbers([1, 2, 3, 4, 5, 6])
    [2, 4, 6]
    
    >>> filter_even_numbers([10, 15, 20, 25])
    [10, 20]
    
    >>> filter_even_numbers([-2, -1, 0, 1, 2])
    [-2, 0, 2]
    """
    return [num for num in numbers if num % 2 == 0]

# write python function to filter even numbers using lambda function
# one-shot learning: add one example in the docstring
def filter_even_numbers_lambda(numbers):

# write assertion tests to test the above functions
if __name__ == "__main__":
    assert filter_even_numbers([1, 2, 3, 4, 5, 6]) == [2, 4, 6]
    assert filter_even_numbers([10, 15, 20, 25]) == [10, 20]
    assert filter_even_numbers([-2, -1, 0, 1, 2]) == [-2, 0, 2]
    
    assert filter_even_numbers_lambda([1, 2, 3, 4, 5, 6]) == [2, 4, 6]
    assert filter_even_numbers_lambda([10, 15, 20, 25]) == [10, 20]
    assert filter_even_numbers_lambda([-2, -1, 0, 1, 2]) == [-2, 0, 2]
    
    print("All tests passed!")