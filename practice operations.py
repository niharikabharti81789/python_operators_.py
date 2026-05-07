
# arithematic operations 
a = 20
b = 30

print(a+b)
print(a-b)
print(a/b) # always answer in float value
print(a*b)
print(a%b) # remainder
print(a**b)# a^b

#relational operators

a=20
b=30
print(a==b) #a is a equals to b --false
print(a!=b) #a is not equals to b -- true
print(a>=b) #a is greater than equals to b -- false
print(a<=b) #a is less than equals to b -- true
print(a>b)  #a is greater than b -- false
print(a<b)  #a is lesser tha b -- true

# assignment operators

num= 10 
num **=10 #num = num+10 # 10+10=20
print("num :",num)

# logical operators

a=2
b=3

print(not False)
print(not(a>b))

val1=True
val2=False
 
print("and operator:", val1 and val2)

print("OR operator:", val1 or val2)
print("OR operator:", (a==b) or (a>b))

# type conversion

a,b= float("2"),3.5
sum= a+b # 2.0+ 3.5 = 5.5
print(sum)
print(type(a))

val = float (input("enter some val"))

print(type(val),val)
a=21
b=27
sum= input("enter a+b =")
 
print("sum:", sum)