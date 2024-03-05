import textwrap

def wrap(string, max_width):
    '''The textwrap module provides some convenience functions, as well as TextWrapper, the class that does all the work. 
    If you’re just wrapping or filling one or two text strings, 
    the convenience functions should be good enough; otherwise, you should use an instance of TextWrapper for efficiency.'''
    return textwrap.wrap(string, max_width)

def fill(string, max_width):
    return textwrap.fill(string, max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    wrap_result = wrap(string, max_width)
    fill_result = fill(string, max_width)
    print(wrap_result,fill_result,sep='\n')
