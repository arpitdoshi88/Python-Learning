# Task
# You have a non-empty set , and you have to execute  commands given in  lines.

# The commands will be pop, remove and discard.

# Input Format

# The first line contains integer , the number of elements in the set .
# The second line contains  space separated elements of set . All of the elements are non-negative integers, less than or equal to 9.
# The third line contains integer , the number of commands.
# The next  lines contains either pop, remove and/or discard commands followed by their associated value.

# Constraints
# 0 < n < 20
# 0 < N < 20


# Output Format

# Print the sum of the elements of set s on a single line.

if __name__ == '__main__':
    n = int(input())
    s = set(map(int, input().split()))
    m = int(input())
    if n < 20 and len(s) <= n:
        commands = list()
        for _ in range(m):
            commands.append(input().split())
        if len(commands) < 20:
            for command in commands:
                try:
                    cmd = command[0]
                    val = command[1] if len(command) > 1 else ""
                    exec(f's.{cmd}({val})')
                except KeyError:
                    pass
            print(sum(s))
        else:
            print('len of commands are more than 20')
    else:
        print('len of n should be less then 20')