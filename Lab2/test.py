import pefile,time

pe = pefile.PE('notepad.exe')
t = time.ctime(pe.FILE_HEADER.TimeDateStamp)
print(pe.dump_info())