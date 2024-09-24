# The first line contains the number of elements in set .
# The second line contains the space separated list of elements in set .
# The third line contains integer , the number of other sets.
# The next  lines are divided into  parts containing two lines each.
# The first line of each part contains the space separated entries of the operation name and the length of the other set.
# The second line of each part contains space separated list of elements in the other set.

# Output Format

# Output the sum of elements in set .

if __name__ == "__main__":
    #print('Enter the length of the first set s')
    n = int(input())
    #print('Enter the elements of the set s')
    s = set(map(int, input().split()))
    #print('Enter the number of other sets')
    m = int(input())
    if len(s) == n:
        for _ in range(m):
            #print('Enter the command and length of the set st')
            command = input().split()
            #print('Enter the elements of the set st')
            st = set(map(int, input().split()))
            if len(command) > 1 and len(st) == int(command[1]):
                exec(f's.{command[0]}({st})')
                #print(s)
    print(sum(s))