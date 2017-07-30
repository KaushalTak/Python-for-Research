
# Dynamic Typing (Revisit the lecture video)

0111100001111 in computer. Tells computer to use 32 bits.

C and C++ are statically typed.

Python is dynamically typed.

Static Typing means that type checking is performed during the vomplie time, whereas dynamic typing means that type checking is performed at run time.

If we tell Python x is equal to 3, how does Python know that x should stand for an integer?

There are three important concepts here: 
- variable 
- object, and 
- reference.

So when you assign variables to objects in Python, the following three things happen.
1. If we type x = 3, the first thing Python will do is create the object, in this case, number 3.
2. Python will do is it will create the variable name, x.
3. Python will insert a reference from the name of the variable to the actual object.

**Variable names and objects are stored in different parts of computer's memory.**

**A key point to remember here is that variable names always link to objects, never to other variables.**

A variable is, therefore, a reference to the given object. In other words, a name is possibly one out of many names that are attached to that object.

When assigning objects, it's useful to keep in mind the distinction between mutable and immutable objects.

Remember, mutable objects, like lists and dictionaries, can be modified at any point of program execution.

In contrast, immutable objects, like numbers and strings, cannot be altered after they've been created in the program.


```python
x = 3
```


```python
y = x
```


```python
y = y-1
```

When we're first asking Python to run the first line, x is equal to 3,
remember the following steps take place. Python first creates the object, 3, then it creates the variable name, x, and, finally it inserts reference from the variable name to the object itself.

When we go and look at the second line, y is equal to x. The object x, in this case number 3, already exists. The next step Python does is it creates a new variable name, which is equal to y, and then it inserts a reference to the object that x, variable name x, is currently referencing.

**Remember, a variable cannot reference another variable. A variable can only reference an object.**

We then will want the third line, which is y equals y minus 1. Python first looks at the object here, which is our number 3. But we know that numbers are immutable. Therefore, in order to do the subtraction, a new object has to be created, which in this case is the number 2. We already have the variable name y in our computer's memory. So the final thing Python does is, it removes y to 3 reference and inserts a reference from y to the object 2.

So once we've run all the these three lines of code, x will eventually be equal to 3 and y will be equal to 2.

Let's then look at **dynamic typing for mutable objects.** The behavior for mutable objects, like lists and dictionaries, looks different, although it really follows the same logic as for immutable objects.
To illustrate the concepts, I've written down three lines of code.


```python
L1 = [2,3,4]
```

Let's start from the first one, L1 is equal to a list which consists of the numbers 2, 3, and 4.
Let's think about what happens as this line is run.
1. Python creates the object-- list 2, 3, 4.
2. Python creates the variable name L1.
3. L1 will reference this list.


```python
L2 = L1
```

The second step, L2 is equal to L1, the object L1 which currently references the list already exists.
Therefore, Python only needs to do two things.
1. It creates the variable name L2. 
2. Because L2 cannot reference L1, which is another variable, it must reference the object that L1 references. Therefore, L2 essentially becomes a synonym for the very same object.


```python
L1[0] = 24
```

L1 application 0 equals 24.
In this case, what happens is we are using the name L1 to reference this object, and we're modifying the content of the number at location 0 from 2 to 24. After this modification, the content of the list is going to be 24, 3, and 4.

By looking at the code here, your first impression might have been that you have two lists, L1 and L2, and only list L1 gets modified.
However, if you understand how dynamic typing works in Python, you have realized that we only have two names that reference the very same object. The last line, L1 at location 0 equals 24 would have been identical to typing L2 at location 0 equals 24.
This is again for the reason that both of these variable names, L1 and L2, reference the very same object. 


```python
L1
```




    [24, 3, 4]




```python
L2
```




    [24, 3, 4]



Each object in Python has a type, value, and an identity.
Mutable objects in Python can be identical in content and yet be actually different objects.
Let's illustrate this point with a simple example.


```python
L = [1,2,3]
```


```python
M = [1,2,3]
```


```python
L == M
```




    True



When we're comparing two lists, the actual comparison
is carried out element-wise. So this 0-th element in L is compared with the 0-th element of M, and so forth.

In this case, the content of these two lists is identical.
Therefore, when I ask, is L equal to M, Python returns "True".
But there is another way how we can compare these two objects.
We can also ask, is L the same object as M?


```python
L is M
```




    False



And in this case, Python returns "False".
What's happening here?


```python
id(L)
```




    84730632




```python
id(M)
```




    84631304




```python
L = [1,2,3]
```


```python
id(L)
```




    84730760




```python
M=L
```


```python
id(M)
```




    84730760




```python
M= list(L)
```


```python
id(M)
```




    84733320



But what if I wanted to create a completely new object that
has identical content to L?
The easiest way to do this is the following. I can ask Python to create a new list, and then assign
that list object to a new variable.
This is the syntax.
I already have my list object, L, in the computer's memory.
By typing list parentheses L, Python will
create a completely new object for me
but the content of that list is going to be identical to the content of list L.
In this case, if I ask, M is L, I get a false. That's because these two objects are distinct. But if I ask, is M equal to L in content,
the answer is going to be true.
Another way to create a copy of a list is to use the slicing syntax.
So I could have said something like, M is equal to L, putting square brackets, and taking every single element from the list L.
This results in the creation of a new list object which is then
assigned to the variable name M.


```python
N = L[:]
```


```python
id(N)
```




    84733768


