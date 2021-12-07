import immlib

def isExecutable(dbugr, args):
    search_instr  = " ".join(args)
    
    search_code   = dbugr.assemble( search_instr )
    results = dbugr.search( search_code )

    dbugr.log('Search_results:', address = 0x5EA2C4)
    for success in results:
        memorypage   = dbugr.getMemoryPageByAddress(success)
        dbugr.log("0x%08x" % success, address = 0x5EA2C4)
    dbugr.log(' ', address = 0xF00D)   
    dbugr.log('Nonexecutables:')    
    for nonexe in results: 
        memorypage   = dbugr.getMemoryPageByAddress(nonexe) 
        access      = memorypage.getAccess(human = True)  
        if "execute" not in access.lower():
            dbugr.log( "Found: %s with access value: %s at 0x%08x" % ( search_instr,access, nonexe ), address = nonexe)
    dbugr.log(' ', address = 0xF00D)
    dbugr.log('Executables:')
    for exe in results:
        memorypage   = dbugr.getMemoryPageByAddress(exe) 
        access      = memorypage.getAccess(human = True)  
        if "execute" in access.lower():
            dbugr.log( "Found: %s with access value: %s at 0x%08x" % ( search_instr,access, exe), address = exe)
                      
    return "Finished searching"

def main(args):
    dbugr          = immlib.Debugger()
    
    result = isExecutable(dbugr, args)
    dbugr.log(' ')
    return result