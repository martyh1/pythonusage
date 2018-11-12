#sys for command line parms and 'quit'
import sys 

def printUsage():
    print("usage: fileOrganize [-y][-t][-v]\n\t-y make changes\n\t-t show changes that *would* be made.\n\t-v verbose")


# tell user must use parms (so this doesn't just make changes to file system right away)
if (len(sys.argv) == 1) or (len(sys.argv) > 4):
    print("Invalid number of arguments")
    printUsage()
    quit()

# save args in readable var names
makeChanges = showChangesOnly = verbose = False
for arg in sys.argv:
    if arg == '-y':
        makeChanges = True
    elif arg == '-t':
        showChangesOnly = True
    elif arg == '-v':
        verbose = True

if not makeChanges and not showChangesOnly:
    print("invalid arguments.  Must use either -t or -y")
    printUsage()
    quit()

#check for conflicting args
if makeChanges and showChangesOnly:
    print("Cannot use -y and -t together.")
    printUsage()
    quit()

#print selections if verbose
if verbose:
    print('Your selections:')
    [print(arg) for arg in sys.argv if arg != sys.argv[0]]

