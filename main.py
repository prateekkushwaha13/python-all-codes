import os
os.system("cls")  # Windows
print("hello i am back")

#comments and multine comments 

#print("hello everyone")
""" hey how are you 
my name is Prateek Kushwaha
 and currently i am pursuing my btech degree from rec kannauj"""

# name = prateek
# age =18
# PythonCoders=35  #camel case
# Pythoncoders=76  #pascal case
# python_coders=47  # snake case (effective way)

#------------ data types -----------------

# numbers

a=20
print(type(a))

b=3/4
print(type(b))

c=12/3
print(type(c))

d=3j
print(type(d))


#boolean


a=True
print(type(a))
b=False
print(type(b))

#unicode conversion
a=65
print(chr(a))
emoji=128512
print(chr(emoji))

b="A"
print(ord(b))
print(ord('s'))





#string 

name="Prateek Kushwaha"
print(name)
print(type(name))

"""any="uieur-eiuh]PW\]4[EP[OJQ7]87Q]5" \
"?Z.X'3PEPQ]W[EP]"
print(type(any))  """

# string indexing 

print(name[0]  ,  name[1],name[2],name[3],name[4],name[5],name[6],name[7],name[8],name[9],name[10],name[11],
      name[12],name[13],name[14],name[15]  )

# string slicing
name = "prateek kushwaha"
print(name[2:5:1])
print(name[:7:1],name[8::1])
print(name[-8:-2:1])   ## it will  printed always right to left
print (name[::-1])  # reverse of the string
print (name[-1:-9:-1])


#------------ type conversion -------------

#explicit type conversion

a=12
print(type(a))
a=str(a)
print(type(a))

a= True
print(type(a))
a=str(a)
print(type(a))

name="hello"
print(type(name))
name=bool(name)
print(name)
print(type(name))

#implicit type conversion

a=12/3
print(a)  # 4.0
print(type(a))   # float

# input and output function in python

a=print(12)
print(type((a)))   # none type

print('hello prateek')

#formatting 
name = "prateek"
age="18"
print("my name is" ,name, "and my age is",age)
print(f"my name is {name} and my age is {age}")

#taking input from the user
# a=input("enter a number: ") 
# print(type(a))   #string
# print(a)

# age= input("enter your age : ")
# print (age)

#------------operators----------------

#arithmetic operators(+,-,*,/,//,**,%)

# a=5
# b=5;
# c=2
# print(a+b,a-c)
# print (a-b)
# print(a*b)
# print(a/b)
# print(a/c)
# print(a*b/c)
# print(a//c)

# comparable operators(<,>,<=,>=,!=,==)

# a=7
# b=4
# c=7
# print(a==b)
# print(a>b)
# print(a<=b)
# print(b<=c)
# print(a!=c)

#logical operators(and ,not, or)   returns one of the operands whether the output is true or false

# print(a<=b and b>2)  #false
# print(34 != 52 or "hello")  # true
# print( "" and hello) # and empty space
# print("hello" or 1)  # hello
# print(5 or 10)  #5
# print (not 5)  # false

# assignment operatiors(=,+=,*=,/=,-=,//=)

# a=5
# a=a+5
# print(a)
# a+=63
# print(a) 
# a*=4
# print(a)

# --------------if,elif,if else------------

# accept two numbers and find greatest between them
# a= input("enter first  number : ")
# b=input("enter second number: ")
# if a>b:
#     print(a,"is greater ")
# elif b>a:
#     print(b,"is greater")    
# else:
#     print(a,b,"both are same")

#   #  accept the gender as char from the user and print greeting message based on the gender

# gender= input("please tell me your gender(M or F) :- ")
# if gender=="M" or gender=="m":
#     print("good morning sir")
# elif gender=="F" or gender=="f":
#     print("good morning mam")
# else :
#     print("unidentified gender")   


# Accept an integer and check whether it is an even number  or odd

# num=int(input("enter a number:- "))
# if num % 2==0:
#     print("number is even")
# else :
#     print ("number is odd")

    #Accept name and age from the user. Check if the user is a valid voter or not.
#   Ex- “hello shery you are a valid voter

# name=input("please enter your name :- ")
# age=int(input("please enter your age:-" ))
# if age>=18:
#     print("hello",name,",you are a valid voter")
# else :
#     print("sorry",name,",you are not a valid voter")  
# 
#  Accept a year and check if it a leap year or not

# year=int(input("enter a year:-"))
# if year % 400==0:
#     print("year is leap year")
# elif year % 100==0:
#     print("year is not a leap year")
# elif year%4==0:
#     print("year is leap year")
# else:
#     print("not a valid year")

# take the input of temperature in celsius
# Below 0°C → "Freezing Cold 
# 0°C to 10°C → "Very Cold 
# 10°C to 20°C → "Cold 
# 20°C to 30°C → "Pleasant 
# 30°C to 40°C → "Hot 
# Above 40°C → "Very Hot "

# temp=int(input("enter a temperature in degree celcius:-"))
# if temp <=0:
#     print("freezing")
# elif temp>0 and temp<=10:
#     print("very cold")
# elif temp>10 and temp<=20:
#     print("cold")
# elif temp>20 and temp<=30:
#     print("pleasant")
# elif temp >30 and temp<=40:
#     print("hot ") 
# elif temp > 40 :
#     print("very hot")            