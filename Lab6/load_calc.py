import my_debugger
from my_debugger_defines import *

debugger = my_debugger.debugger()
exePath2Load = "c:\\windows\\system32\\calc.exe".encode("utf-8")

debugger.load(exePath2Load)

