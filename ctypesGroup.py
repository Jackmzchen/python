mystr = """">>> from ctypes import *
>>> print('\\n')
>>> def message(str1):
>>>     \\tlent = len(str1)
>>>     \\tprint('#'*(lent+4))
>>>     \\tprint('# '+str1+' #')
>>>     \\tprint('#'*(lent+4))
>>> print('\\n')
>>> libfunc = CDLL('#path#')
>>> ret = libfunc.divide(100, 8)
div: 12.500000
>>> print('Returned value: ', ret)
>>> ret
15
>>> libfunc.divide.restype = c_float
>>> ret = libfunc.divide(100, 8)
div: 12.500000
>>> print('Returned value: ', ret)
>>> ret
12.5
>>> ret = libfunc.divide(100, 7)
div: 14.285714
>>> ret
14.285714149475098
>>> print('Returned value: ', ret)
>>> print('\\n')
>>> libfunc.multiply.argtypes = [c_int, c_float, c_int]
>>> libfunc.multiply(10, 20, 30)
mul: -1451888896
17
>>> print('\\n')
>>> try:
>>>     \\tlibfunc.multiply(10, 'aaa', 30)
>>> except ArgumentError as e:
>>>     \\tprint('There was an error', e)

>>> libfunc.multiply.argtypes = [c_int, c_int, c_int]
>>> libfunc.multiply(10, 20, 30)
mul: 6000
10
>>> libfunc.multiply.restype = None
>>> libfunc.multiply(10, 20, 30)
mul: 6000
>>> mystr2 = "WHY aren't the lines below this getting evaluated??? HOW can the code be fixed to resolve this?????"
>>> message(mystr2)
>>> libfunc.divide(33.4, 5)
>>> libfunc.divide(20, 3)
"""

import re
import os
import sys

path = input("Please enter the absolute path to the libfunc.so file: ")

if not os.path.isfile(path):
    print("Library file: {file} doesn't exist. \nQUITTING ...")
    sys.exit(-1)

with open('cTypes.py', 'w') as myfile:
    values = re.finditer(r'[>]{3}\s+(.*)', mystr)
    for value in values:
        if "print('\\n')" in value.group(1):
            myfile.write('\n')
        elif value.group(1) != 'ret':
            if '\\t' in value.group(1):
                myfile.write('\t' + value.group(1).replace('\\t', '')+'\n')
            elif '#path#' in value.group(1):
                myfile.write(value.group(1).replace('#path#', path) + '\n')
            else:
                myfile.write(value.group(1)+'\n')