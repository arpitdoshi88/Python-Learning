# Task
# The students of District College have subscriptions to English and French newspapers. Some students have subscribed only to English, some have subscribed to only French and some have subscribed to both newspapers.

# You are given two sets of student roll numbers. One set has subscribed to the English newspaper, and the other set is subscribed to the French newspaper. The same student could be in both sets. Your task is to find the total number of students who have subscribed to at least one newspaper.

# Input Format

# The first line contains an integer, , the number of students who have subscribed to the English newspaper.
# The second line contains  space separated roll numbers of those students.
# The third line contains , the number of students who have subscribed to the French newspaper.
# The fourth line contains  space separated roll numbers of those students.

# Constraints

# 0 < total number of students in collecge < 1000

# Output Format

# Output the total number of students who have subscriptions to both English and French newspapers.

if __name__ == '__main__':
    n = int(input())
    a = set(map(int, input().split()))
    m = int(input())
    b = set(map(int, input().split()))
    print(len(a.intersection(b)))