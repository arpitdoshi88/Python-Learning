## Ms. Gabriel Williams is a botany professor at District College. One day, she asked her student Mickey to compute the average of all the plants with distinct heights in her greenhouse.
### avg = sum of distinct heights / total distinct height
## input n = 10, arr = 16 15 16 17 18 20 21 22 23 20

def average(array):
    # your code goes here
    distinctArr = set(array) ## this will return a set of distinct heights
    return sum(distinctArr)/len(distinctArr)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)