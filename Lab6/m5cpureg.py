from my_debugger_defines import *
import my_debugger

debugger = my_debugger.debugger()

pid = int(input("Please enter the PID of the process to attach to: "))

debugger.attach(pid)
print('Process PID: ', pid)

for values in debugger.enumerate_threads():
    registers = debugger.get_thread_context(values)
    print('Dumping regs for thread ID: ', hex(values))
    print('EIP: ', hex(registers.Rip))
    print('ESP: ', hex(registers.Rsp))
    print('EBP: ', hex(registers.Rbp))
    print('EAX: ', hex(registers.Rax))
    print('EBX: ', hex(registers.Rbx))
    print('ECX: ', hex(registers.Rcx))
    print('EDX: ', hex(registers.Rdx))
    
debugger.detach()