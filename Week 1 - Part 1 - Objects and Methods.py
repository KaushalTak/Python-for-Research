
# coding: utf-8

# ## Modules and Methods

# In[4]:

import math


# In[5]:

math.pi


# In[6]:

math.sqrt(10)


# If we just need the value of pi from the math module. Then

# In[7]:

from math import pi
math.pi


# **Namespace**
# Namespace is a container of names shared by objects that typically go together. Helps in preventing naming conflicts.
# Example:

# In[9]:

import math


# In[15]:

import numpy as np


# The functions with same names in these two modules will have different namespace.

# In[12]:

math.sqrt(10)


# In[16]:

np.sqrt(10)


# In[17]:

np.sqrt([1,2,3,44,55])


# In[18]:

math.sqrt([1,2,3,44,55])


# **What happens when you import new module?** 
# **1** Python creates new namespace for all the objects which are defined in the new module.
# 
# **2** Python than executes the code of the module and it runs it within this newly created namespace.
# 
# **3** It creates a name lets say np for numpy and this name references this new namespace object(ex np.sqrt in numpy namespace).

# **Finding type of object**

# In[20]:

name = "Amy"


# In[21]:

type(name)


# In[22]:

dir(name)


# In[23]:

dir(str)


# **help** Finding about the function

# In[24]:

help(name.upper)


# No, help(name.upper()). Don't run the method.

# ## Numbers and Basic Calculations##
# 
# There are three different numeric types:
# - Integer (indefinite precision)
# - Float
# - Complex

# In[25]:

1234 ** 5555


# In[26]:

6/7


# In[27]:

15/7


# In[28]:

15//7


# In[29]:

15//8


# In[30]:

15 / 2.3


# In[31]:

_


# In[32]:

_ * 2.3


# In[33]:

import math


# In[34]:

math.factorial(3)


# ## Random Choice ##
# 
# Simple random samples
# 

# In[35]:

import random


# In[36]:

random.choice([2,444,44,66,77])


# Python doesn't care about type of objects in random.choice

# In[37]:

random.choice(["11", "dd", "55"])


# ## Exxpressions and Booleans##
# 
# Expression is a combination of objects and operators that computes a value.
# Many expressions involve what is known as **Boolean** data type. They have only two values:
# - TRUE
# - FALSE

# In[38]:

type(True)


# Only three Boolean operations:
# - OR
# - AND
# - NOT

# In[39]:

True or False


# In[40]:

True or False


# In[41]:

True and False


# In[42]:

not True


# In[43]:

2 < 44


# In[44]:

2 == 2


# In[45]:

2 != 2


# In[46]:

[10, 5] > [10, 10]


# In[47]:

[10, 5] > [9, 10]


# In[48]:

[10, 5] > [11, 4]


# In[49]:

[10, 5] > [122, 4]


# In[50]:

[2, 3] == [3, 3]


# In[51]:

[2, 3] is [2, 3]


# It means we have two objects. Even when they have same numbers.

# In[53]:

[2,2,2] > [1,1,3]


# In[54]:

[2,2,2] > [3,3,2]


# In[55]:

2.0 == 2.0


# In[56]:

2 == 2.0


# Python here converts 2, the integer, into a float and then compares.

# **==** tests whether objects have the same value, whereas **is** tests whether objects have the same identity.

# In[ ]:



