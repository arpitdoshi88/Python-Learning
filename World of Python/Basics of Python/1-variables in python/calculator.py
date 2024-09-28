print("########### Calcculator ######################")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > 0 and num2 > 0:
    print("Enter 1 for addition, 2 for subtraction, 3 for multiplication, 4 for division,5 for floor division")    
    i = int(input("Enter your choise: "))
    if i==1:
        print("Addition of two numbers",num1+num2)
    elif i==2:
        print("Subtraction of two numbers",num1-num2)
    elif i==3:
        print("Multiplication of two numbers",num1*num2)
    elif i==4:        
        print("Division of two numbers",num1/num2)
    elif i==5:
        print("Floor of two numbers",num1//num2)
    else: print("Please provide correct choice")
else:
    print("Please enter a number > 0")