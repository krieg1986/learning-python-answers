Python 3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> def echo(o):
...         print(o)
... 
...         
>>> echo('s')
s
>>> echo(4)
4
>>> echo([1,2,3,4])
[1, 2, 3, 4]
>>> echo({'a':1, 'b':2, 'c':3})
{'a': 1, 'b': 2, 'c': 3}
>>> echo()
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    echo()
TypeError: echo() missing 1 required positional argument: 'o'
>>> echo('s', 'b')
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    echo('s', 'b')
TypeError: echo() takes 1 positional argument but 2 were given
