#an operator is a special character or symbol that tells a computer to do with a variable
#age is called the variable
#the '=' sign is called an operator that tells the value of a declaration
#we have 6 sets of operators
#1.Arithmetic operators
#2.assignment operators
#3.logical
#4.comparison
#5.bitwise
#6.special

num1,num2 = 20,30
print(num1+num2)
print(num1/num2)
print(num1*num2)
print(num2-num1)

#other arithmetic operators include
#floor division we use 2 division signs. after division, we take the whole number without decimal places
#modulo (means the remainder after a calculation)
#exponential ** (Value of num1 to the power of num2)

#modulo % means the remainder after division
print(num1%num2)
print(25 // 3)

#assignment operators are such as: =, +=, -=, **=, %=, /=
var1=10
var2=20
var1 += var2
print(var1) #this means that var1= var1 + var2

#comparison operators: >, <, >=, <=, ==
var3=8
var4=7
print("check whether var3 is same as var4", var3==var4)

#the and operator will work if all conditions are true
print((var3>2) and (var4<var3))

print(True and True)
print(True and False)
print(True or False)
print(True or True)
print(False or False)
print(not True)
print(not False)