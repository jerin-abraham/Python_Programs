# -*- coding: utf-8 -*-
"""Tuple_DS_Programs.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_3raRqnAPYwdrtSxSA4RF5r27rTl_uoE
"""

#The parentheses are optional but it is good practice to use.
#Note: The tuple which is created without using parentheses is also known as tuple packing.
t='sting','jerin',1,24,25
t
#type(t)

#Creating a tuple with single element is slightly different. We will need to put comma after the element to declare the tuple.

tup1 = ("JavaTpoint")  
print(type(tup1))  
#Creating a tuple with single element   
tup2 = ("JavaTpoint",)  
print(type(tup2))

#Write a Python program to create a tuple with numbers and print one item.
tup1=(1,2,4,5,9)
print('whole tuple',tup1)
print('one item from tuple',tup1[2])

#Write a Python program to unpack a tuple in several variables.
tup2=(1,2,4,5,9,10,11)
print('elements of tuple')
for i in tup2:
  print(i)

#Write a Python program to add an item in a tuple.
#create a tuple
tuplex = (4, 6, 2, 8, 3, 1) 
print(tuplex)
#tuples are immutable, so you can not add new elements
#using merge of tuples with the + operator you can add an element and it will create a new tuple
tuplex = tuplex + (9,)
print(tuplex)
#adding items in a specific index
tuplex = tuplex[:5] + (15, 20, 25) + tuplex[:5]
print(tuplex)
#converting the tuple to list
listx = list(tuplex) 
#use different ways to add items in list
listx.append(30)
tuplex = tuple(listx)
print(tuplex)

#Write a Python program to convert a tuple to a string.
tup = ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')
str =  ''.join(tup)
print(str)