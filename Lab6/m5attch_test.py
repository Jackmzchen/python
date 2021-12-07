import my_debugger , keyboard
from my_debugger_defines import *
from ctypes import *

kernel32 = windll.kernel32

debugcheck = False
debug_event = DEBUG_EVENT()

pid = int(input("Please enter the PID of the process to attach to: "))

debugger = my_debugger.debugger()

debugger.attach(pid)
while True:
    if kernel32.WaitForDebugEvent(byref(debug_event),100):
        debug = debug_event.dwDebugEventCode
        if debugcheck == False and debug >= 0x1:                                                        #prints only the first debug event that occurs
            print("Debug Event Code: %d" % debug)
            debugcheck = True
        else:
            kernel32.ContinueDebugEvent(debug_event.dwProcessId, debug_event.dwThreadId, DBG_CONTINUE)       
    if keyboard.is_pressed('q') == True and debugcheck == True:
        debugger.detach()
        exit(-1)
