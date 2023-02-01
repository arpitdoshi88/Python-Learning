#In Python, operators are special symbols that designate that some sort of computation should be performed. The values that an operator acts on are called operands.

a = 9
b = 2
print(a+b)  # here a and b are operands and "+" is operator

#An operand can be either a literal value or a variable that references an object:
#Below are arithmatic operators supported by python
# +(unary)  +a
# +(binary)  a + b
# -(unary)  -a
# -(binary) a - b
# * multiplication
# / division
# //floor division
# % Modulo
# ** exponentiation 
print()

print('+(unary)',+a)
print('+(binary)',a+b)
print('-(unary)',-a)
print('-(binary)',a-b)
print('multiplication',a*b)
print('division',a/b)
print('modulo',a%b)
print('floor division',a//b)
print('exponentiation',a**2)

#The result of standard division (/) is always a float, even if the dividend is evenly divisible by the divisor:
print()
print(8/4)
print(type(8/4))

#When the result of floor division (//) is positive, it is as though the fractional portion is truncated off, leaving only the integer portion. 
#When the result is negative, the result is rounded down to the next smallest (greater negative) integer:

print()
print(10/4)
print(10//4)
print(10//-4)
print(-10//4)
print(-10//-4)
print()

##comparision operators
##it always returns boolean
# == equal to operator... returms True if value of a is equal to the value of b
# != not equal to operator..returms True if value of a is not equal to the value of b
# < less than..True if value of a is less than b
# <= less than or qual to..True if value of a is less than or equal to b
# > greater than..True if value of a is greater than b
# >= greater than or qual to..True if value of a is greater than or equal to b

print(5==5)
print(5!=5)
print(3<5)
print(5<5)
print(5<=5)
print(3>5)
print(5>5)
print(5>=5)
print()

##value stored internally for a float object may not be precisely what you’d think it would be. For that reason, it is poor practice to compare floating-point values for exact equality
a = 1.1 + 1.1
print(a == 2.2)

#the preferred way to determine whether two floating-point values are “equal” is to compute whether they are close to one another, given some tolerance
tolerance = 0.000001
x = 1.1+2.2
print(abs(x-3.3)<tolerance)