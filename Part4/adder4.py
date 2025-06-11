def adder(**kwargs):
    sum = 0
    value = kwargs.values()
    for i in value:
        sum += i
    return sum
adder(red=3, blue=4, green=6, purple=9)
print(adder(red=3, blue=4, green=6, purple=9))