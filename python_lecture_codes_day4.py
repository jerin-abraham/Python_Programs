# -*- coding: utf-8 -*-
"""Python_Lecture_Codes.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Wb3Zq1lXFirjL6up8rXrc8itv5_PVyTP
"""

print("Hello world!")

INR=float(input("Enter amount in INR:"))
USD=INR/73.05
print("Amount in USD:",USD)

Amount=float(input("Enter Amount:"))
Year=float(input("Enter Year:"))
ROI=float(input("Enter Rate of Interest"))/100
Interest=Year*ROI*Amount
Total_Amount=Amount+Interest
print("Amount after",Year,"is", Total_Amount)

s=int(input("Enter time in secs:"))
h=s//3600

m=(s%3600)//60

s=(s%3600)%60
print("HH:",h,"MM:",m,"SS:",s)

HH=int(input("Enter time in Hours:"))
MM=int(input("Enter time in Minutes:"))
SS=int(input("Enter time in Seconds:"))
HH=HH*60*60
MM=MM*60
Total_Seconds=SS+HH+MM
print("Time in Seconds:",Total_Seconds)

feet=float(input("Enter Height in Fts:"))
inch=feet*12
cm=2.5*inch
print("Height in Centimetre:",cm)

height=float(input("Height in cms = "))
feet = height//(12*2.5)
inch = (height%12)//2.5
print("feet:",int(feet),"inch:",int(inch))

#Please write the code for the following
#1. To input two numbers and print maximum amongst two.
#2. To input length and breadth of a rectangle and calculate and print area and perimeter.
#3. To input Principal,Time and rate of interest. Calculate and print Simple interest.
#4. To accept age of a person and check whether the person is Major(Above 18) or Minor.
#5. To accept a number and check whether it is a positive no or negative number.

no1,no2,no3=int(input("Enter num1:")),int(input("Enter num2:")),int(input("Enter num3:"))
if(no1<no2 and no1<no3):
  print("Min is:",no1)
elif no2<no3:
  print("Min is:",no2)
else:
  print("Min is:",no3)

P=float(input("Enter Percentage:"))
if P>=60:
  print("first")
elif 50<=P and P<60:
  print("Second")
elif 40<=P and P<50:
  print("pass")
else:
  print("fail")

# Python3 code to demonstrate working of
# Get Month Name from Month Number
# Using calendar library and month number
import calendar
  
# initializing month number
test_num = int(input("Enter month Number:"))
               
# printing original month number
print("The original month number is : " + str(test_num))
  
# using month_name() to get month name 
res = calendar.month_name[test_num]
  
# printing result
print("Month Name from Number : " + str(res))

for i in range(1,6,1):
  print("x"*i)

for i in range(1,6,1):
  print(" "*i,'x')

for i in range(1,6,1):
  print(" "*(6-i),'x'*i)

for i in range(1,6,1):
  print(" "*(6-i),' x'*i)

for i in range(5,0,-2):
  print(" "*(6-i),' x'*i)

w=input("Enter word:")
for i in range(1,len(w)+1):
  print(w[:i])

w=input("Enter word:")
n=len(w)
for i in range(1,len(w)+1):
  print(" "*(n-i),w[:i])

w=input("Enter word: ")
for i in w:
  print(i,'-->',ord(i))

line=input("Enter a sentence: ")
wordlist=line.split()
wordlist=wordlist[::-1]
rline=''
for i in wordlist:
  rline=rline+" "+i
  print(rline)
print(rline)

line=input("Enter a sentence: ")
wordlist=line.split()
rline=wordlist[::-1]
if wordlist==rline:
  print("yes palindrome sentence")
else:
  print("not a palindrome sentence")

line=input("Enter sentence: ")
wlist=line.split()
wset=set(wlist)
print("Total words: ",len(wlist),"Total unique words given by:",len(wset))
for i in wset:
  print(i,"-->",wlist.count(i))