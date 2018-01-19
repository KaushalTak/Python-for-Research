# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 18:40:49 2018

@author: Kaushal
"""

import pandas as pd

x = pd.Series([6,3,8,6])

x = pd.Series([6,3,8,6], index = ["q", "w", "e", "r"])

x[["w", "e"]]

#Creating a pandas series by passing a dictionary

age = {"Tim": 29, "Jim": 31, "Pam":27, "Sam":35}

x = pd.Series(age)

data = {'name' : ["Tim", "Jim", "Pam", "Sam"],
        'age': [29, 31,27,35],
        'ZIP': ['02115', '02130', '67700', '00100']}


X = pd.DataFrame(data, columns=["name", "age", "ZIP"])

X["name"]

X.name

x = pd.Series([6,3,8,6], index = ["q", "w", "e", "r"])
x.index

sorted(x.index)

x.reindex(sorted(x.index))

x = pd.Series([6,3,8,6], index = ["q", "w", "e", "r"])
y = pd.Series([7,3,5,2], index = ["e", "q", "r", "t"])

x + y