##variables in python are case sensitive
##it can be of any length but cannot start with digits
##it can have underscores or Unicode characters

#In Python everything is object

#what happens when you initialize a variable in python as below
n=100 ##python interpreter will create an object with value 100 and it will give the pointer or reference tp the object with name n
print(n)
print()
#multiple variable assignment
m=n=100  ## interpreter will create only one object and both m and n will point to this same object with value 100
print(m , n)
print()

##multiple assignment
a,b = 10,20  # for multiple assignment no of variables in left side must be same as no of values in right side of assignment operator
print(a , b)  
print()
##object identity
print(id(a))
print(id(b))
print()
## small integer caching
##python caches small integer from -5 to 256. It creates int object for this value in the memory as these numbers are mostly used many times
m= 300
n = 300
print(m is n)
print(id(m) is id(n))
print()

a=100
b=100
print(a is b)
print(id(a) is id(b))

###
a,b= 250,250

for _ in range(250,260):
    if a != b:
        print(id(a) , id(b))
        break
    a += 1
    b += 1
print(a)

##orphan objects in python are cleared from the memory thrugh garbage collection
m=100
n=100
m= n = 150 #so integer object of value 100 is now orphaned and it will be cleared from the memory through gc

##python 3.7 has 35 reserved keywords which cannot be used as a variable names
help("keywords")