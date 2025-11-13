# Input Format

# The first line contains the space separated elements of set .
# The second line contains integer , the number of other sets.
# The next  lines contains the space separated elements of the other sets.

# Output Format

# Print True if set  is a strict superset of all other  sets. Otherwise, print False.

if __name__ == "__main__":
    a = set(map(int,input().split()))
    n = int(input())
    isStrictSuperset = True
    for _ in range(n):
        s = set(map(int,input().split()))
        if not a.issuperset(s):
            isStrictSuperset = False
    print(isStrictSuperset)