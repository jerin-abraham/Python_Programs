# -*- coding: utf-8 -*-
"""Assignment_150_problems.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-GG2__pp6XYQ0_r8xoVMj6jcNs5YcLLH
"""

import sys
print("Python Verison")
print(sys.version)
print("Version info.")
print(sys.version_info)

import datetime
now=datetime.datetime.now()
print("Current data and time:")
print(now)  #.strftime())

fname=input("Input your first name: ")
lname=input("Input your last name: ")
print("Hello "+lname+ " "+fname)

rad=float(input("Enter the radius of the circle: "))
print("the area of the circle with radius ",rad," is ",float(3.14*rad*rad))

values=input("Input some comma separated numbers: ")
list=values.split(',')
tuple=tuple(list)
print('List: ',list)
print('Tuple: ',tuple)



l=[]
while True:
  data=input("enter values: ")
  if data==' ':
    break
  l.append(data)

print(l)
tup1=tuple(l)
print(tup1)

filename=input("Input the filename: ")
f_extnms=filename.split(".")
print("The extension of the file is : ",f_extnms[-1])

color_list=["Red","Green","White","Black"]
print(color_list[0],color_list[-1])

exam_st_date=(11,12,2014)
#type(exam_st_date)
print("The examination will start from : %i / %i / %i"%exam_st_date)

i=int(input("Enter a number:"))
num= (i+ ((i*10)+i) + ((i*100)+(i*10)+i))
print(num)


n=int(input("Enter a number n: "))
temp=str(n)
t1=temp+temp
t2=temp+temp+temp
comp=n+int(t1)+int(t2)
print("The value is:",comp)

print(abs.__doc__)

import calendar
y=int(input("Input the year: "))
m=int(input("Input the month: "))
print(calendar.month(y,m))

from datetime import date
f_date = date(2014, 7, 2)
l_date = date(2014, 7, 11)
delta = l_date - f_date
print(delta.days)

#Write a Python program to get the volume of a sphere with radius 6.
pi = 3.1415926535897931
r= float(input("Enter radiues of the sphere: "))
V= 4.0/3.0*pi* r**3
print('The volume of the sphere is: ',V)

#Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference.
n=int(input("Enter number: "))
r=n-17
if n>17:
  print(r*2)
else:
  print(abs(r))

#Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference.
def difference(n):
    if n <= 17:
        return 17 - n
    else:
        return (n - 17) * 2 

print(difference(22))
print(difference(14))

#Write a Python program to test whether a number is within 100 of 1000 or 2000.
def limit(n):
  if n<100:
    print("The number you have entered is within the range of 100")
  elif n > 100 and n <= 1000:
    print("The number you have entered is within the range of 1000")
  elif n <= 2000:
    print("The number you have entered is within the range of 2000")
  else:
    print("Your value exceeds the limit. ")

x = int(input("Enter the number here: "))
limit(x)

#Write a Python program to calculate the sum of three given numbers
#if the values are equal then return thrice of their sum.
n,n2,n3=int(input("Enter num1: ")),int(input("Enter num2: ")),int(input("Enter num2: "))

if n!=n2!=n3:
  print(n+n2+n3)
elif n==n2==n3:
  print(3*(n+n2+n3))

#Write a Python program to get a new string from a given string where "Is" has been added to the front.
#If the given string already begins with "Is" then return the string unchanged.

def str_check(str):
  str=input("Enter a string: ")
  if len(str)>=2 and str[:2]=='IS':
    return str
  return 'IS' + str

str_check(str)

#Write a Python program to get a string which is n (non-negative integer) copies of a given string.
n=input("Enter non-negative integer: ")
str=input("Enter a string: ")
n=int(n)
print(n*str)

#Write a Python program to find whether a given number (accept from the user) is even
#or odd, print out an appropriate message to the user

n=int(input("Enter number: "))
if n%2==0:
  print(n,' is a even number')
else:
  print(n,' is a odd number')

#Write a Python program to count the number 4 in a given list.

l=[]
counter=0
while True:
  data=input("enter values: ")
  if data==' ':
    break
  l.append(data)
print(l)
for i in l:
  if int(i)==4:
    counter=counter+1

print("The count of 4 in the entered list is: ", counter)

#Write a Python program to get the n (non-negative integer) copies of the first 2 
#characters of a given string. Return the n copies of the whole string if the length is less than 2.

n=int(input("Enter non-negative integer: "))
str=input("Enter a string: ")
#def string_check(n):
if n>2:
  print(n*str[0:2])
else:
  print(n*str)

#string_check(n)

#Write a Python program to test whether a passed letter is a vowel or not.
l=['A','E','I','O','U','a','e','i','o','u']
str=input("Enter a character: ")
counter=0
for i in l:
  if i==str:
    counter+=1

if counter==1:
  print("Given character is a vowel")
elif counter==0:
  print("Given character is not a vowel")

#Write a Python program to check whether a 
#specified value is contained in a group of values.
l=[]
counter=0
while True:
  data=input("enter values: ")
  if data==' ':
    break
  l.append(data)
num=input("Enter the value you want to search in the group: ")
for i in l:
  if i==num:
    counter+=1

if counter==1:
  print("Entered number is present in the group")
else:
  print("Entered number is not present in the group")

#Write a Python program to create a histogram from a given list of integers.
l=[]
sy='@'
while True:
  data=input("enter values: ")
  if data==' ':
    break
  l.append(data)
for i in l:
  print(sy*int(i))

#Write a Python program to concatenate all elements in a list into a string and return it.
l=[]
string=''
while True:
  data=input("enter values: ")
  if data==' ':
    break
  l.append(data)
for i in l:
  string+=i
print(string)

#Write a Python program to print out all even numbers from a given numbers list in the same order
#and stop the printing if any numbers that come after 237 in the sequence.
numbers = [    
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527
    ]

for x in numbers:
    if x == 237:
        print(x)
        break;
    elif x % 2 == 0:
        print(x)

#Write a Python program to print out a set containing all the colors from color_list_1 
#which are not present in color_list_2.
s1={'Green','Blue','Black','Grey','Yellow'}
s2={'White','Green','Red','Blue'}
print(s1-s2)

l={}
l=set()
while True:
  data=input("enter values: ")
  if data==' ':
    break
  l.add(data)

type(l)

#Write a Python program that will accept the base and height of a triangle and compute the area.

h=float(input("Enter height: "))
b=float(input("Enter base: "))
a=0.5*h*b
print("Area of Triangle is:",a)

#Write a Python program to compute the greatest common divisor (GCD) of two positive integers.

#Write a Python program to get the least common multiple (LCM) of two positive integers.

#Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.
n1,n2,n3=int(input("Enter num1: ")),int(input("Enter num2: ")),int(input("Enter num3: "))
if n1==n2 or n2==n3 or n1==n3:
  print('Sum = ',0)
else:
  print("Sum = ",n1+n2+n3)

#Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20.

n1,n2=int(input("Enter num1: ")),int(input("Enter num2: "))
sum=n1+n2
if sum>=15 and sum<=20:
  print(20)
else:
  print("Sum is: ",sum)

#Write a Python program which will return true if the two given integer values are equal or their sum or difference is 5.

n1,n2=int(input("Enter num1: ")),int(input("Enter num2: "))
if n1==n2 or n1-n2==5 or n1+n2==5:
  print(True)
else:
  print(False)

#Write a Python program to add two objects if both objects are an integer type.
n1,n2=int(input("Enter num1: ")),int(input("Enter num2: "))

if type(n1)==int and type(n2)==int:
  print(n1+n2)
else:
  print("Objects must be of integer type")

#Write a Python program to add two objects if both objects are an integer type.
def add_numbers(a, b):
   if not (isinstance(a, int) and isinstance(b, int)):
       return "Inputs must be integers!"
   return a + b
print(add_numbers(10, 20))
print(add_numbers(10, 20.23))
print(add_numbers('5', 6))
print(add_numbers('5', '6'))

#Write a Python program to display your details like name, age, address in three different lines.
name,age,address=input("Enter Name: "),int(input("Enter Age: ")),input("Enter Address: ")
print('Name : ',name,'\nAge : ',age,'\nAddress : ',address)

#Write a Python program to solve (x + y) * (x + y).
x,y=int(input("Enter x: ")),int(input("Enter y: "))
z=(x+y)*(x+y)
print('(',x,' + ',y,') ^ ',2,') = ',z)

#Write a Python program to compute the future value of a specified principal amount, rate of interest, and a number of years.
amt = 10000
int = 3.5
years = 7
future_value = amt*((1+(0.01*int)) ** years)
print(round(future_value,2))

#Write a Python program to compute the distance between the points (x1, y1) and (x2, y2).

#Write a Python program to check whether a file exists.
import os.path
print(os.path.isfile('main.txt'))
print(os.path.isfile('main.py'))

#Write a Python program to determine if a Python shell is executing in 32bit or 64bit mode on OS.
# For 32 bit it will return 32 and for 64 bit it will return 64
import struct
print(struct.calcsize("P") * 8)

#Write a Python program to get OS name, platform and release information.
import platform
import os
print("Name of the operating system:",os.name)
print("\nName of the OS system:",platform.system())
print("\nVersion of the operating system:",platform.release())

#Write a Python program to locate Python site-packages.
import site; 
print(site.getsitepackages())

#Write a python program to call an external command in Python.
import os
print(os.system('ls -l'))

#Write a python program to get the path and name of the file that is currently executing.
import os
print("Current File Name : ",os.path.realpath(__file__))

#Write a Python program to find out the number of CPUs using.
import multiprocessing
print(multiprocessing.cpu_count())

#Write a Python program to parse a string to Float or Integer.
n =input("Enter number:")
print(float(n))
print(int(float(n)))

#Write a Python program to list all files in a directory in Python.

#Write a Python program to print without newline or space.
for i in range(0, 10):
    print('*', end="")
print("\n")

#Write a Python program to determine profiling of Python programs.

#Write a Python program to print to stderr.

#Write a python program to access environment variables.

#Write a Python program to get the current username

#Write a Python to find local IP addresses using Python's stdlib

#Write a Python program to get height and width of the console window.

#Write a Python program to get execution time for a Python method.

#Write a python program to find the sum of the first n positive integers.

#Write a Python program to convert height (in feet and inches) to centimeters.

#Write a Python program to calculate the hypotenuse of a right angled triangle.

#Write a Python program to convert the distance (in feet) to inches, yards, and miles.

#Write a Python program to convert all units of time into seconds.

#Write a Python program to get an absolute file path.

#Write a Python program to get file creation and modification date/times.

#Write a Python program to convert seconds to day, hour, minutes and seconds.

#Write a Python program to calculate body mass index.

#Write a Python program to convert pressure in kilopascals to pounds per square inch, a millimeter of mercury (mmHg) and atmosphere pressure.

#Write a Python program to calculate the sum of the digits in an integer.

# Write a Python program to sort three integers without using conditional statements and loops.