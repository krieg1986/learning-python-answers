import sys, traceback
from Q2 import oops
def safe(func, *pargs, **kargs):
    pass
try:
    safe(oops())
except Exception:
    print(sys.exc_info()[0])
    traceback.print_exc(file=open('error.txt', 'w'))