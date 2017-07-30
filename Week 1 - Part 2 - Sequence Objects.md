
# Sequences

In Python, a sequence is a collection of objects ordered by their position.
In python there are three basic sequences:
- Lists
- Tuples
- Range Objects

Python also has additional sequence types for representing things like strings.

The crucial aspect about sequences is that any sequence data type will support the common sequence operations. But, in addition, these different types will have their own methods available.

The sequence indexing starts with zero for the first element of sequence - Sequence[0] (To access first element). Another way to access element by giving negative numbers.

** Slicing**

Sequence[0:2] gives first and second element. This is called slicing. :p

** Quiz on Sequences **

Q 1: Consider the following tuple and index (1,2,3)[-0]. What will this return?


```python
(1,2,3)[-0]
```




    1



A 1: Counting from index 0, this moves backwards 0 steps, which is still index 0. For this tuple, this returns value 1.

** Q 2: Consider the following tuple and index (1,2,3)[-0:0]. What will this return? **


```python
(1,2,3)[-0:0]
```




    ()



Python includes all values from the beginning of the first index in the slice up to and not including the second value in the slice. In this case, the slice contains not indeces, not even 0, so it returns an empty tuple.

# Lists

Lists are ** mutable sequences of objects of any type. ** Typically used to store homogenous items.

They are just like strings but there differences. Like, strings are sequences of individual characters, whereas lists are sequences of any type of python objects.

Strings: Immutable
Lists: Mutable


```python
numbers = [2, 4, 6, 8]
```


```python
numbers[1]
```




    4




```python
numbers[0:3]
```




    [2, 4, 6]




```python
numbers[-2]
```




    6



** Append Method for lists **


```python
numbers.append(10)
```


```python
numbers
```




    [2, 4, 6, 8, 10]



** Concatenate **


```python
x = [12, 14, 16]
```


```python
numbers + x
```




    [2, 4, 6, 8, 10, 12, 14, 16]




```python
type(_)
```




    list




```python
numbers = numbers + x
```

** Reverse **


```python
numbers
```


```python
 numbers.reverse()
```

Lists methods are in-place methods. They don't return anything, like the one above didn't.


```python
numbers
```

It takes last object and moves it to first, then take 1st object and move it to first. Then 2nd last to second then 2nd to second last. And so on.

** Sort**


```python
names  = ["Zofia", "Sofia", "Amy"]
```


```python
names.sort()
```


```python
names
```




    ['Amy', 'Sofia', 'Zofia']



** Sorted **

Asking python to create a completly new list, not like **sort**. New list created using the old one.


```python
names.reverse()
```


```python
names
```




    ['Zofia', 'Sofia', 'Amy']




```python
sorted_names = sorted(names)
```


```python
names
```




    ['Zofia', 'Sofia', 'Amy']




```python
sorted_names
```




    ['Amy', 'Sofia', 'Zofia']



**len - Finding Length**


```python
len(names)
```




    3



# Tuples

Tuples : Immutable.
Typically used to store **hetrogenous data**.

Can view it as a single object that consists of several different parts.

** Uses of tuple**

** When you want to return more than one object from your python function. Wrap those objects in one tuple object and then return that tuple.**


```python
T = (1, 3, 5, 7)
```


```python
len(T)
```




    4




```python
T + (9, 11)
```




    (1, 3, 5, 7, 9, 11)




```python
T[1]
```




    3



How to pack unpacked tuples?


```python
xxx = 122.23
```


```python
yyy = 22.55
```


```python
coordinate = (xxx, yyy)
```


```python
type(coordinate)
```




    tuple



**Unpacking** ***(Important)***


```python
coordinate
```




    (122.23, 22.55)




```python
(c1, c2) = coordinate
```


```python
c1
```




    122.23




```python
c2
```




    22.55




```python
coordinates = [(1,2), (3,4), (5,6)]
```


```python
for (x,y) in coordinates:
    print(x,y)
```

    1 2
    3 4
    5 6
    


```python
x
```




    5




```python
for x, y in coordinates:
    print (x, y)
```

    1 2
    3 4
    5 6
    


```python
c = (2,3)
```

**How to create tuple with one object?**


```python
type(c)
```




    tuple




```python
c = (2)
```


```python
type(c)
```




    int




```python
c = (2,)
```


```python
type(c)
```




    tuple




```python
c = 2,
```


```python
type(c)
```




    tuple



We cant add any number to tuple coz they are immutable.

**Count Method**


```python
x = (1,3,3,2)
```


```python
x.count(3)
```




    2




```python
sum(x)
```




    9



# Ranges #

Immutable sequences of integers.

Used in for loops.


```python
range(5)
```




    range(0, 5)




```python
list(range(5))
```




    [0, 1, 2, 3, 4]




```python
list(range(1,6))
```




    [1, 2, 3, 4, 5]




```python
list(range(1,13,2))
```




    [1, 3, 5, 7, 9, 11]



When we use range python only stores 1, 13, 2. But when we use list then all the numbers.

** Ranges do not instantiate their elements, making them more efficient in loops.
**

# Strings

Immutable


```python
S = "Python"
```


```python
len(S)
```




    6




```python
S[0]
```




    'P'




```python
S[-1]
```




    'n'




```python
S[0:3]
```




    'Pyt'




```python
S[-3:]
```




    'hon'




```python
S[-3:0]
```




    ''



**Testing membership**


```python
"y" in S
```




    True




```python
"L" in  S
```




    False



**Ploymorphism**

Polymorphism means that what an operator does depends on the type of objects it is being applied to.

** Addition (Polymorphism) **


```python
12 + 12
```




    24



Concatenate


```python
"hello" + "world"
```




    'helloworld'



**Multiplication (Polymorphism)**


```python
S = "Python"
```


```python
3*S
```




    'PythonPythonPython'




```python
3*_ + "."
```




    'PythonPythonPythonPythonPythonPythonPythonPythonPython.'




```python
dir(str)
```




    ['__add__',
     '__class__',
     '__contains__',
     '__delattr__',
     '__dir__',
     '__doc__',
     '__eq__',
     '__format__',
     '__ge__',
     '__getattribute__',
     '__getitem__',
     '__getnewargs__',
     '__gt__',
     '__hash__',
     '__init__',
     '__init_subclass__',
     '__iter__',
     '__le__',
     '__len__',
     '__lt__',
     '__mod__',
     '__mul__',
     '__ne__',
     '__new__',
     '__reduce__',
     '__reduce_ex__',
     '__repr__',
     '__rmod__',
     '__rmul__',
     '__setattr__',
     '__sizeof__',
     '__str__',
     '__subclasshook__',
     'capitalize',
     'casefold',
     'center',
     'count',
     'encode',
     'endswith',
     'expandtabs',
     'find',
     'format',
     'format_map',
     'index',
     'isalnum',
     'isalpha',
     'isdecimal',
     'isdigit',
     'isidentifier',
     'islower',
     'isnumeric',
     'isprintable',
     'isspace',
     'istitle',
     'isupper',
     'join',
     'ljust',
     'lower',
     'lstrip',
     'maketrans',
     'partition',
     'replace',
     'rfind',
     'rindex',
     'rjust',
     'rpartition',
     'rsplit',
     'rstrip',
     'split',
     'splitlines',
     'startswith',
     'strip',
     'swapcase',
     'title',
     'translate',
     'upper',
     'zfill']




```python
str.replace
```




    <method 'replace' of 'str' objects>




```python
?_
```


```python
name = "Kaushal Tak"
```


```python
name.replace("T", "t")
```




    'Kaushal tak'




```python
name
```




    'Kaushal Tak'



**Splitting**


```python
type(name)
```




    str




```python
len(name)
```




    11




```python
names = name.split(" ")
```


```python
type(names)
```




    list




```python
len(names)
```




    2




```python
names[0]
```




    'Kaushal'




```python
type(names[0])
```




    str




```python
names[0].upper()
```




    'KAUSHAL'




```python
names
```




    ['Kaushal', 'Tak']



** Quiz **


```python
"".join([str(i) for i in range(10)])

```




    '0123456789'




```python
str(range(10))

```




    'range(0, 10)'




```python
string.digits (using the string library)
```


      File "<ipython-input-102-94544475d2f2>", line 1
        string.digits (using the string library)
                               ^
    SyntaxError: invalid syntax
    



```python
import string
```


```python
string.digits
```




    '0123456789'




```python
dir(string)
```




    ['Formatter',
     'Template',
     '_ChainMap',
     '_TemplateMetaclass',
     '__all__',
     '__builtins__',
     '__cached__',
     '__doc__',
     '__file__',
     '__loader__',
     '__name__',
     '__package__',
     '__spec__',
     '_re',
     '_string',
     'ascii_letters',
     'ascii_lowercase',
     'ascii_uppercase',
     'capwords',
     'digits',
     'hexdigits',
     'octdigits',
     'printable',
     'punctuation',
     'whitespace']




```python
string.ascii_lowercase
```




    'abcdefghijklmnopqrstuvwxyz'




```python
string.printable
```




    '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'




```python
string.whitespace
```




    ' \t\n\r\x0b\x0c'




```python
string.hexdigits
```




    '0123456789abcdefABCDEF'




```python
string.octdigits
```




    '01234567'



** Checking if string only contains digits**


```python
"1234667890000".isdigit()
```




    True




```python
"1234667890000".isdigit
```




    <function str.isdigit>



# Sets


```python
Sets are unordered collections of distinct hashable objects.
```

** Hashable **

It means that you can use sets for immutable objects like number and strings, but not for mutable objects like lists and dictionaries.

There are **two types of sets**
- Set (Mutable)
- Frozen Set (Not Mutable)

**Properties of sets**

1. **They cannot be indexed.**
2. Elements cannot be duplicated. What it means is all the objects in the set are going to be distinct or unique.

** Sets are used for**

- Unions
- Intersections
- Set Differences


```python
ids = set()
```


```python
ids = set([1,2,3,4])
```


```python
len(ids)
```




    4




```python
ids.add(10)
```


```python
ids
```




    {1, 2, 3, 4, 10}




```python
ids.add(2)
```


```python
ids
```




    {1, 2, 3, 4, 10}



**Removing objects from sets**


```python
ids.pop()
```




    1




```python
ids.pop()
```




    2




```python
ids = set(range(10))
```


```python
ids
```




    {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}




```python
males = set([1, 2,7,8])
```


```python
females = ids - males
```


```python
females
```




    {0, 3, 4, 5, 6, 9}



**Set Union**


```python
everyone = males | females
```


```python
_
```




    {0, 3, 4, 5, 6, 9}




```python
everyone
```




    {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}



** Intersection **


```python
everyone & set([1,100,3,5])
```




    {1, 3, 5}



**Sets for counting Unique Letters in words**


```python
words = "aaaaaaaaaaaaaaasssssssdedefrgtggthyjuj"
```


```python
len(words)
```




    38




```python
letters = set(words)
```


```python
len(letters)
```




    12



Let sets x={1,2,3} and y={2,3,4}. How could you get {4} from x and y using basic set operations?

**Simply y-x will do the trick. y.difference(x) works as well!**

** Consider again sets x={1,2,3} and y={2,3,4}. How could you get {1, 4} from x and y using basic set operations?**

**x.symmetric_difference(y) performs this task.**

Consider again sets x={1,2,3} and y={2,3,4}. Which following lines of code will determine if all elements of x are in y?

**x.issubset(y)**

# Dictionaries

Dictionaries are mapping from key objects to value objects.

Conists of key:value pairs, where,
- Key:immutable
- Value : anythings

Dictionaries can be used for performing very fast lookup on unordered data. They are not sequences. Do not maintain order.


```python
age = {}
```


```python
type(age)
```




    dict




```python
age = dict()
```


```python
age = {"Tim": 29, " Jim": 67}
```


```python
age["Tim"]
```




    29




```python
age["Tim"] = age["Tim"] + 1
```


```python
age["Tim"] += 1
```


```python
age["Tim"]
```




    31




```python
age["Tim"] =+ 1
```


```python
age["Tim"]
```




    1




```python
dir(dict)
```




    ['__class__',
     '__contains__',
     '__delattr__',
     '__delitem__',
     '__dir__',
     '__doc__',
     '__eq__',
     '__format__',
     '__ge__',
     '__getattribute__',
     '__getitem__',
     '__gt__',
     '__hash__',
     '__init__',
     '__init_subclass__',
     '__iter__',
     '__le__',
     '__len__',
     '__lt__',
     '__ne__',
     '__new__',
     '__reduce__',
     '__reduce_ex__',
     '__repr__',
     '__setattr__',
     '__setitem__',
     '__sizeof__',
     '__str__',
     '__subclasshook__',
     'clear',
     'copy',
     'fromkeys',
     'get',
     'items',
     'keys',
     'pop',
     'popitem',
     'setdefault',
     'update',
     'values']




```python
age.keys
```




    <function dict.keys>



**Contents of dict_keys and dict_values objects change we change the parent dictonary. **


```python
names = age.keys()
```


```python
type(names)
```




    dict_keys




```python
age["Tim"]
```




    1




```python
age["Lol"] = 3
```


```python
age
```




    {' Jim': 67, 'Lol': 3, 'Tim': 1}




```python
names
```




    dict_keys(['Tim', ' Jim', 'Lol'])




```python
ages = age.values()
```


```python
ages
```




    dict_values([1, 67, 3])




```python
age["Nick"] = 31
```

Testing Membership


```python
"Tim" in  age
```




    True




```python
"Tim" in names
```




    True



**Only immutable types are allowed as keys.**
