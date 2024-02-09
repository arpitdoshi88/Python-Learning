def count_substring(string, sub_string):
    count = [string[i:].startswith(sub_string) for i in range(len(string))]
    print(count)
    return sum(count)
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)