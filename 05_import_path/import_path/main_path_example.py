import os
import sys
from pprint import pprint

"""
https://www.youtube.com/watch?v=0oTh1CXRaQ0&ab_channel=PyCon2015
"""

print("\nsys.path")
for x in sys.path:
    print(x)

print("\n -- Current path -- ")
print(__file__)

print("\n -- PYTHONPATH -- ")
for x in os.getenv("PYTHONPATH").split(os.pathsep):
    print(x)

print("\n -- prefix -- ")
print(sys.prefix)  # tämä löytyy python.exen sijainnin perusteella


pprint(sys.modules)

"""
python -vv
import socket
"""