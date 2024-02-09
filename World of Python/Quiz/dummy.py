def print_formatted(number):
    # your code goes here
    max_width = len(bin(number)[2:])
    for i in range(1,number+1):
        decimalNumber = str(i).rjust(max_width)
        octNumber = oct(i)[2:].rjust(max_width)
        hexNumber = hex(i)[2:].upper().rjust(max_width)        
        binNumber = bin(i)[2:].rjust(max_width)
        print(decimalNumber,octNumber,hexNumber,binNumber,sep=' ')

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)