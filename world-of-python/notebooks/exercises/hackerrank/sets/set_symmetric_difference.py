def get_sd(a,b):
    return sorted(a.symmetric_difference(b))

if __name__ == '__main__':
    n =  int(input())
    a = set(map(int, input().split()))
    m = int(input())
    b = set(map(int, input().split()))
    sd = get_sd(a,b)
    for i in sd:
        print(i)
    
    2