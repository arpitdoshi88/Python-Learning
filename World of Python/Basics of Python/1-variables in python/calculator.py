num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > 0 and num2 > 0:
    print("Addition of two numbers",num1+num2)
    print("Subtraction of two numbers",num1-num2)
    print("Multiplication of two numbers",num1*num2)
    print("Division of two numbers",num1/num2)
    print("Floor of two numbers",num1//num2)
else:
    print("Please enter a number > 0")