import immlib

def main(args):
    debger = immlib.Debugger()
    
    countargs = 0
    debger.log("Running m07p02.py")
    debger.log("Program args are:")
    for x in args:
        debger.log('Arg[%d]: %s' % (countargs,x))
        countargs += 1
        
    return ("pycommand executed with %d commands" % countargs)