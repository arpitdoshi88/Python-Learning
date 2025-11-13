# You are given two sets,  and .
# Your job is to find whether set  is a subset of set .

# If set  is subset of set , print True.
# If set  is not a subset of set , print False.

# Input Format

# The first line will contain the number of test cases, .
# The first line of each test case contains the number of elements in set .
# The second line of each test case contains the space separated elements of set .
# The third line of each test case contains the number of elements in set .
# The fourth line of each test case contains the space separated elements of set .

# Output Format

# Output True or False for each test case on separate lines.
if __name__ == '__main__':
    noOfTests = int(input())
    for _ in range(noOfTests):
        noOfElemtsinA = int(input())
        a = set(map(int, input().split()))
        noOfElemtsinB = int(input())
        b = set(map(int, input().split()))
        print(a.issubset(b))