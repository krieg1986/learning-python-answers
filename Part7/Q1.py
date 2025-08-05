def oops():
    raise IndexError()
try:
    oops()
except IndexError:
    pass
