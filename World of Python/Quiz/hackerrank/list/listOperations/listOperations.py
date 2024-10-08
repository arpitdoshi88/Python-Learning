# Input Format

# The first line contains an integer, , denoting the number of commands.
# Each line  of the  subsequent lines contains one of the commands described above.

# Constraints

# The elements added to the list must be integers.
# Output Format

# For each command of type print, print the list on a new line.

if __name__ == '__main__':
    N = int(input())
    commands = {}
    _lst =[]
    for _ in range(N):
        command , *args = input().split()
        if command == 'append':
            _lst.append(int(args[0]))
        elif command == 'insert':
            _lst.insert(int(args[0]),int(args[1]))
        elif command == 'sort':
            _lst.sort()
        elif command == 'pop':
            _lst.pop()
        elif command == 'remove':
            _lst.remove(int(args[0]))
        elif command == 'reverse':
            _lst.reverse()
        elif command == 'print':
            print(_lst)
        else:
            print(_lst)
