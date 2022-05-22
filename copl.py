python3
Python 3.8.10 (default, Mar 15 2022, 12:22:08) 
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 4*=2
  File "<stdin>", line 1
SyntaxError: cannot assign to literal
>>> b=4
>>> b*=2
>>> b
8
>>> c=2
>>> *c=2
  File "<stdin>", line 1
SyntaxError: starred assignment target must be in a list or tuple
>>> p=[3,4,5]
>>> *x,=p
>>> x
[3, 4, 5]
>>> x==p
True
>>> x is p
False
>>> #wooooow python nice 
>>> #creating a copy of list
>>> w=[2,4,5,6]
>>> *p,=w
>>> p
[2, 4, 5, 6]
>>> p==w
True
>>> p is w
False

