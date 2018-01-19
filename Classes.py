# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 01:13:19 2018

@author: Kaushal
"""

#When you find that an existing object doesn't fully suit your needs, in which
#case you can create a new type of object known as a class. Often it is that case
#that even if you need to create a new object type, it is likely that this new
#object type resembles, in some way, an exisiting one.

#Inheritance
#Inheritance means that you can define a new object type, a new class, that 
#inherits properties from an existing object type. For example, you coukd
#define a class that does everything that Python's built-in lists do, and then
#add an additional method or methods, based on your needs.

ml = [5,9,3,6,8,11,4,3]

ml.sort()

ml


class MyList(list): #MyList is inherting properties from the object type list
#You can think of the class statement as setting up a kind of blueprint of a
#new class. What that means is that it specifies the internal structure of these new
#types of objects, including what methods and operations they support, but
#it does not create any object of that type. When an object of particular type is
#created that object is sometimes called an "Instance" of that type.
#So, the class statement does not create any instances of the class. This is bit like
#defining a function with the "def" statement, the function defination specifies what the
#function does when called but defining a function does not, in itself, call or invoke 
#that function. That's something you would do outside of the functions defination.
#That's why it's helpful to think of the class statement as defining a blueprint of
#of the new class, a new type of python object.

x = [5,2,9,11,10,2,7]
min(x)

max(x)

x.remove(2) #only removes the first occurence of the 2 
x    

class MyList(list):
    def remove_min(self):       #The functions defined inside a class are known
        self.remove(min(self))  #as "instance methods" because they operate on an
    def remove_max(self):       #instance of the class. By convention, the name of the
        self.remove(max(self))  #class instance is called "self", and it is always 
                                #passed as the first argument to the functions defined
                                #as part of a class.

x = [5,2,9,11,10,2,7]

y = MyList(x)

dir(x)
dir(y)

y.remove_min()

y.remove_max()






