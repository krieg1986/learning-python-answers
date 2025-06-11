def adder(o, *o1):
    sum = 0
    for s in o1:
        sum = sum + o + s
    return sum
adder(1,2,3,4,5)
print(adder(1,2,3,4,5))
adder('b','c','e','f')
print(adder('b','c','e','f'))
adder({'a':1, 'b':2, 'c':3})
print(adder({'a':1, 'b':2, 'c':3}))
