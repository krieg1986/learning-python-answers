import sys
class MyError(Exception):
    pass
def oops():
    raise IndexError()
    raise NameError()
try:
    oops()
except IndexError:
    import sys
    print((type(sys.exception()), sys.exception))
except MyError:
    print((type(sys.exception()), sys.exception))
    