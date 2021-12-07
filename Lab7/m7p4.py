import immlib

def findString(allstrings, tofind):
    foundstr = []
    for string in allstrings:
       if string[1].find(tofind) !=-1 or string[2].find(tofind) != -1:
            templst = [string[0]]
            foundstr.append(templst)
    if not foundstr:
        return "No Matches Found"
    return foundstr

def findMyFun(immdbg, myaddrList):
    addrList = []
    for addr in myaddrList:
        for addr in addr:
            addrList.append(immdbg.getFunctionBegin(addr))
    return addrList

def SetBpRun(immdbg, myaddrList):
    filterList = []                                                         #filters the extras that are brought over from the addresses
    for items in myaddrList:
        if items not in filterList and items != 0:
            filterList.append(items)
    for address in filterList:
        bp = immdbg.setBreakpoint(address)
        immdbg.log('Set breakpoint at %x' % address, address = address)
    immdbg.log("Attempting to run the program...", address = 0x37A27)
    immdbg.run()
    immdbg.log("Stopping at breakpoint",address = 0x57099ED)

def main(args):
    dbugr = immlib.Debugger() 
    allstrings = dbugr.getReferencedStrings(dbugr.getCurrentAddress())
    #dbugr.log('%s: %s' % (type(allstrings), allstrings), address=0xB337F00D)
    #for string in allstrings:
       # dbugr.log('    %s - %s - %s' % (string[0], string[1], string[2]))
    foundstr = findString(allstrings, args[0])
    address = findMyFun(dbugr,foundstr)
    if not args or foundstr == "No Matches Found":
        dbugr.log("No string found/entered")
        return "Done"
    else:
        for string in foundstr:
            dbugr.log("Found %s at 0x%x" % (args[0], string[0]), address = string[0])
        for addr in address:
            dbugr.log("Function begins at: 0x%x" % addr, address = addr)
        bp = SetBpRun(dbugr,address)
        return"Done !!!" 