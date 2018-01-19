# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 00:08:23 2018

@author: Kaushal
"""

#Scope Rules
#Python searches for the object, layer by layer, moving from inner layers towards
#outer layers, and it uses the first update function or the first x variable that it
#finds.

#Scope Rule
#LEGB
#Local
#Enclosing function
#Global
#Built-in

#In other words, local is the current function you are in.
#Enclosing function is the function that called the current function, if any.
#Global refers to the module in which the function was defined.
#And Built-in refers to Python's buit-in namespace

#We can manipulate global variables, variables defined in the global scope, from within
#functions.



#Mutability, Immutability and Scope Rules
def update(n,x):
    n = 2
    y = x
    y.append(2)
    print('update:', n, y)
    
def main():
    n = 1
    x = [0,1,2,3]
    print('main:', n, x)
    update(n,x)
    print('main:', n, x)
    
    
main()

#An arguement is an object that is passed to a function as its input when the
#function is called.
#A parameter, in cotrast, is a variable that is used in the function defination
#to refer to that arguement.

some_guy = 'Fred'

first_names = []
first_names.append(some_guy)

print(some_guy is first_names[0])

another_list_of_names = first_names
another_list_of_names.append('George')
some_guy = 'Bill'


first_names = ['Fred', 'George', 'Bill']
last_names = ['Smith', 'Jones', 'Williams']
name_tuple = (first_names, last_names)

first_names.append('Igor')

print (some_guy, first_names, another_list_of_names)