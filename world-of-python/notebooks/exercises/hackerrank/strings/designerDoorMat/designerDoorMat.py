###
# Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:
#
# Mat size must be X. ( is an odd natural number, and  is  times .)
# The design should have 'WELCOME' written in the center.
# The design pattern should only use |, . and - characters.
if __name__ == '__main__':
     dim = list(map(int,input().split()))
     n,m = dim[0],dim[1]
     _str = 'WELCOME'
     c = '.|.'
     top_range = int(n/2)
     for i in range(top_range):
        print((c*i).rjust(int(m/2)-1,'-')+c+(c*i).ljust(int(m/2)-1,'-'))
     print(_str.center(m,'-'))
     for i in range(top_range-1,-1,-1):
        print((c*i).rjust(int(m/2)-1,'-')+c+(c*i).ljust(int(m/2)-1,'-'))