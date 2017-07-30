
# coding: utf-8

# # Sequences

# In Python, a sequence is a collection of objects ordered by their position.
# In python there are three basic sequences:
# - Lists
# - Tuples
# - Range Objects

# Python also has additional sequence types for representing things like strings.

# The crucial aspect about sequences is that any sequence data type will support the common sequence operations. But, in addition, these different types will have their own methods available.

# The sequence indexing starts with zero for the first element of sequence - Sequence[0] (To access first element). Another way to access element by giving negative numbers.

# ** Slicing**

# Sequence[0:2] gives first and second element. This is called slicing. :p

# ** Quiz on Sequences **

# Q 1: Consider the following tuple and index (1,2,3)[-0]. What will this return?

# In[4]:

(1,2,3)[-0]


# A 1: Counting from index 0, this moves backwards 0 steps, which is still index 0. For this tuple, this returns value 1.

# ** Q 2: Consider the following tuple and index (1,2,3)[-0:0]. What will this return? **

# In[5]:

(1,2,3)[-0:0]


# Python includes all values from the beginning of the first index in the slice up to and not including the second value in the slice. In this case, the slice contains not indeces, not even 0, so it returns an empty tuple.

# # Lists

# Lists are ** mutable sequences of objects of any type. ** Typically used to store homogenous items.

# They are just like strings but there differences. Like, strings are sequences of individual characters, whereas lists are sequences of any type of python objects.

# Strings: Immutable
# Lists: Mutable

# In[6]:

numbers = [2, 4, 6, 8]


# In[7]:

numbers[1]


# In[8]:

numbers[0:3]


# In[9]:

numbers[-2]


# ** Append Method for lists **

# In[10]:

numbers.append(10)


# In[11]:

numbers


# ** Concatenate **

# In[12]:

x = [12, 14, 16]


# In[13]:

numbers + x


# In[14]:

type(_)


# In[ ]:

numbers = numbers + x


# ** Reverse **

# In[ ]:

numbers


# In[ ]:

numbers.reverse()


# Lists methods are in-place methods. They don't return anything, like the one above didn't.

# In[ ]:

numbers


# It takes last object and moves it to first, then take 1st object and move it to first. Then 2nd last to second then 2nd to second last. And so on.

# ** Sort**

# In[22]:

names  = ["Zofia", "Sofia", "Amy"]


# In[24]:

names.sort()


# In[25]:

names


# ** Sorted **

# Asking python to create a completly new list, not like **sort**. New list created using the old one.

# In[26]:

names.reverse()


# In[27]:

names


# In[28]:

sorted_names = sorted(names)


# In[29]:

names


# In[30]:

sorted_names


# **len - Finding Length**

# In[31]:

len(names)


# # Tuples

# Tuples : Immutable.
# Typically used to store **hetrogenous data**.

# Can view it as a single object that consists of several different parts.

# ** Uses of tuple**

# ** When you want to return more than one object from your python function. Wrap those objects in one tuple object and then return that tuple.**

# In[33]:

T = (1, 3, 5, 7)


# In[34]:

len(T)


# In[35]:

T + (9, 11)


# In[36]:

T[1]


# How to pack unpacked tuples?

# In[37]:

xxx = 122.23


# In[38]:

yyy = 22.55


# In[39]:

coordinate = (xxx, yyy)


# In[40]:

type(coordinate)


# **Unpacking** ***(Important)***

# In[41]:

coordinate


# In[42]:

(c1, c2) = coordinate


# In[43]:

c1


# In[44]:

c2


# In[45]:

coordinates = [(1,2), (3,4), (5,6)]


# In[46]:

for (x,y) in coordinates:
    print(x,y)


# In[47]:

x


# In[49]:

for x, y in coordinates:
    print (x, y)


# In[50]:

c = (2,3)


# **How to create tuple with one object?**

# In[51]:

type(c)


# In[52]:

c = (2)


# In[53]:

type(c)


# In[54]:

c = (2,)


# In[55]:

type(c)


# In[56]:

c = 2,


# In[58]:

type(c)


# We cant add any number to tuple coz they are immutable.

# **Count Method**

# In[59]:

x = (1,3,3,2)


# In[60]:

x.count(3)


# In[61]:

sum(x)


# # Ranges #

# Immutable sequences of integers.

# Used in for loops.

# In[63]:

range(5)


# In[64]:

list(range(5))


# In[65]:

list(range(1,6))


# In[66]:

list(range(1,13,2))


# When we use range python only stores 1, 13, 2. But when we use list then all the numbers.

# ** Ranges do not instantiate their elements, making them more efficient in loops.
# **

# # Strings

# Immutable

# In[67]:

S = "Python"


# In[68]:

len(S)


# In[69]:

S[0]


# In[70]:

S[-1]


# In[71]:

S[0:3]


# In[72]:

S[-3:]


# In[74]:

S[-3:0]


# **Testing membership**

# In[75]:

"y" in S


# In[76]:

"L" in  S


# **Ploymorphism**

# Polymorphism means that what an operator does depends on the type of objects it is being applied to.

# ** Addition (Polymorphism) **

# In[78]:

12 + 12


# Concatenate

# In[80]:

"hello" + "world"


# **Multiplication (Polymorphism)**

# In[81]:

S = "Python"


# In[82]:

3*S


# In[83]:

3*_ + "."


# In[84]:

dir(str)


# In[85]:

str.replace


# In[86]:

get_ipython().magic('pinfo _')


# In[87]:

name = "Kaushal Tak"


# In[89]:

name.replace("T", "t")


# In[90]:

name


# **Splitting**

# In[91]:

type(name)


# In[92]:

len(name)


# In[93]:

names = name.split(" ")


# In[94]:

type(names)


# In[95]:

len(names)


# In[96]:

names[0]


# In[97]:

type(names[0])


# In[98]:

names[0].upper()


# In[99]:

names


# ** Quiz **

# In[100]:

"".join([str(i) for i in range(10)])


# In[101]:

str(range(10))


# In[102]:

string.digits (using the string library)


# In[106]:

import string


# In[108]:

string.digits


# In[109]:

dir(string)


# In[112]:

string.ascii_lowercase


# In[113]:

string.printable


# In[114]:

string.whitespace


# In[115]:

string.hexdigits


# In[116]:

string.octdigits


# ** Checking if string only contains digits**

# In[119]:

"1234667890000".isdigit()


# In[120]:

"1234667890000".isdigit


# # Sets

# In[ ]:

Sets are unordered collections of distinct hashable objects.


# ** Hashable **

# It means that you can use sets for immutable objects like number and strings, but not for mutable objects like lists and dictionaries.

# There are **two types of sets**
# - Set (Mutable)
# - Frozen Set (Not Mutable)

# **Properties of sets**

# 1. **They cannot be indexed.**
# 2. Elements cannot be duplicated. What it means is all the objects in the set are going to be distinct or unique.

# ** Sets are used for**

# - Unions
# - Intersections
# - Set Differences

# In[121]:

ids = set()


# In[122]:

ids = set([1,2,3,4])


# In[123]:

len(ids)


# In[125]:

ids.add(10)


# In[126]:

ids


# In[127]:

ids.add(2)


# In[128]:

ids


# **Removing objects from sets**

# In[129]:

ids.pop()


# In[130]:

ids.pop()


# In[133]:

ids = set(range(10))


# In[134]:

ids


# In[135]:

males = set([1, 2,7,8])


# In[136]:

females = ids - males


# In[138]:

females


# **Set Union**

# In[140]:

everyone = males | females


# In[141]:

_


# In[143]:

everyone


# ** Intersection **

# In[144]:

everyone & set([1,100,3,5])


# **Sets for counting Unique Letters in words**

# In[150]:

words = "aaaaaaaaaaaaaaasssssssdedefrgtggthyjuj"


# In[151]:

len(words)


# In[148]:

letters = set(words)


# In[149]:

len(letters)


# Let sets x={1,2,3} and y={2,3,4}. How could you get {4} from x and y using basic set operations?

# **Simply y-x will do the trick. y.difference(x) works as well!**

# ** Consider again sets x={1,2,3} and y={2,3,4}. How could you get {1, 4} from x and y using basic set operations?**

# **x.symmetric_difference(y) performs this task.**

# Consider again sets x={1,2,3} and y={2,3,4}. Which following lines of code will determine if all elements of x are in y?

# **x.issubset(y)**

# # Dictionaries

# Dictionaries are mapping from key objects to value objects.

# Conists of key:value pairs, where,
# - Key:immutable
# - Value : anythings

# Dictionaries can be used for performing very fast lookup on unordered data. They are not sequences. Do not maintain order.

# In[152]:

age = {}


# In[153]:

type(age)


# In[154]:

age = dict()


# In[155]:

age = {"Tim": 29, " Jim": 67}


# In[156]:

age["Tim"]


# In[157]:

age["Tim"] = age["Tim"] + 1


# In[158]:

age["Tim"] += 1


# In[159]:

age["Tim"]


# In[160]:

age["Tim"] =+ 1


# In[161]:

age["Tim"]


# In[162]:

dir(dict)


# In[163]:

age.keys


# **Contents of dict_keys and dict_values objects change we change the parent dictonary. **

# In[168]:

names = age.keys()


# In[169]:

type(names)


# In[165]:

age["Tim"]


# In[166]:

age["Lol"] = 3


# In[167]:

age


# In[170]:

names


# In[171]:

ages = age.values()


# In[172]:

ages


# In[173]:

age["Nick"] = 31


# Testing Membership

# In[174]:

"Tim" in  age


# In[176]:

"Tim" in names


# **Only immutable types are allowed as keys.**
