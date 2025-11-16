if __name__ == '__main__':
    s = input()
    f1,f2,f3,f4,f5 = False,False,False,False,False
    f1 = any([char.isalnum() for char in s])
    f2 = any([char.isalpha() for char in s])
    f3 = any([char.isdigit() for char in s])
    f4 = any([char.islower() for char in s])
    f5 = any([char.isupper() for char in s])
    print(f1,f2,f3,f4,f5,sep='\n')