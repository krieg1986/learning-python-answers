Python 3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
2**16
65536
2/5, 2/5.0
(0.4, 0.4)
'hack' + 'code'
'hackcode'
S = 'Python'
'grok ' + S
'grok Python'
S * 5
'PythonPythonPythonPythonPython'
S[0], S[:0], S[1:]
('P', '', 'ython')
how = 'fun'
'coding %s is %s!' % (S, how)
'coding Python is fun!'
'coding {} is {}!'.format(S, how)
'coding Python is fun!'
f'coding {S} is {how}!'
'coding Python is fun!'
('x',)[0]
'x'
('x', 'y')[1]
'y'
L = [1, 2, 3] +[4, 5, 6]
L, L[:], L[:0], L[-2], L[-2:]
([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [], 5, [5, 6])
([1, 2, 3] + [4, 5, 6])[2:4]
[3, 4]
[L[2], L[3]]
[3, 4]
L.reverse(); L
[6, 5, 4, 3, 2, 1]
L.sort(); L
[1, 2, 3, 4, 5, 6]
L.index(4)
3
{'a' : 1, 'b': 2}['b']
2
D = {'x': 1, 'y': 2, 'z': 3}
D['w'] = 0
D['x'] + D['w']
1
D[(1, 2, 3)] = 4
list(D.keys()), list(D.values()), (1, 2, 3) in D
(['x', 'y', 'z', 'w', (1, 2, 3)], [1, 2, 3, 0, 4], True)
[[]], ["", [], (), {}, None]
([[]], ['', [], (), {}, None])
L = [0, 1, 2, 3]
l[4]
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    l[4]
NameError: name 'l' is not defined. Did you mean: 'L'?
L[-1000:100]
[0, 1, 2, 3]
L[3:1]
[]
L[3:1]=[4]
L
[0, 1, 2, 4, 3]
L = [1, 2, 3, 4]
L[2] =[]
L[2:3]=[]
del L[1:]
L[0:2]=1
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    L[0:2]=1
TypeError: must assign iterable to extended slice
L[1:2]=1
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    L[1:2]=1
TypeError: must assign iterable to extended slice
X = 'code'
Y = 'hack'
X, Y = Y, X
D = {}
D[1] = 'a'
D[2]='b'
D[(1, 2, 3)] = 'c'
D
{1: 'a', 2: 'b', (1, 2, 3): 'c'}
k=['a', 'b', 'c']
D = dict.fromkeys(k)
D['d']
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    D['d']
KeyError: 'd'
D['d']='hack'
'hack' + [1, 2, 3]
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    'hack' + [1, 2, 3]
TypeError: can only concatenate str (not "list") to str
(1, 2, 3) + [1, 2, 3]
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    (1, 2, 3) + [1, 2, 3]
TypeError: can only concatenate tuple (not "list") to tuple
'hack' + {a:2, b:3, c:4}
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    'hack' + {a:2, b:3, c:4}
NameError: name 'a' is not defined
D = {}
D = {a:2, b:3, c:4}
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    D = {a:2, b:3, c:4}
NameError: name 'a' is not defined
'hack' + {'a':2, 'b':3, 'c':4}
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    'hack' + {'a':2, 'b':3, 'c':4}
TypeError: can only concatenate str (not "dict") to str
L
[1]
M = L.append(3)
M = S.append(s)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    M = S.append(s)
AttributeError: 'str' object has no attribute 'append'
M = L.append(s)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    M = L.append(s)
NameError: name 's' is not defined. Did you mean: 'S'?
M = L.append('s')
L.keys()
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    L.keys()
AttributeError: 'list' object has no attribute 'keys'
S + S
'PythonPython'
L + L
[1, 3, 's', 1, 3, 's']
S[:]
'Python'
L[:]
[1, 3, 's']
S = 'hack'
S[0][0][0][0][0]
'h'
S=['h','a','c','k']
S[0][0][0][0][0]
'h'
S = 'hack'
S[1:2]=e
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    S[1:2]=e
NameError: name 'e' is not defined
S[1:2]='e'
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    S[1:2]='e'
TypeError: 'str' object does not support item assignment
S[0:1] + 'e' + S[2:]
'heck'
S[1]='e'
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    S[1]='e'
TypeError: 'str' object does not support item assignment
D = {}
>>> D={name=['mark', 'john', 'trevor'], 'age'=26, 'job'='database engineer', 'address'='300 gint street', 'email'='wiser@msn.com', 'phone number'='876-300-3543'}
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
>>> D={'name'=['mark', 'john', 'trevor'], 'age'=26, 'job'='database engineer', 'address'='300 gint street', 'email'='wiser@msn.com', 'phone number'='876-300-3543'}
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
>>> D={'name':['mark', 'john', 'trevor'], 'age':26, 'job':'database engineer', 'address':'300 gint street', 'email':'wiser@msn.com', 'phone number':'876-300-3543'}
>>> D
{'name': ['mark', 'john', 'trevor'], 'age': 26, 'job': 'database engineer', 'address': '300 gint street', 'email': 'wiser@msn.com', 'phone number': '876-300-3543'}
>>> D[name]
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    D[name]
NameError: name 'name' is not defined
>>> D['name']
['mark', 'john', 'trevor']
>>> D['age']
26
>>> D['job']
'database engineer'
>>> file = open ('myfile.txt', 'w')
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    file = open ('myfile.txt', 'w')
PermissionError: [Errno 13] Permission denied: 'myfile.txt'
>>> file=open('myfile.txt', 'w')
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    file=open('myfile.txt', 'w')
PermissionError: [Errno 13] Permission denied: 'myfile.txt'
