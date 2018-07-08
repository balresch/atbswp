from builtins import print as normalprint

def print(text, *args):
    lengthOfLongestLine = len(text)
#    if type(args[0]) == list:
    for arg in args:
        for arg in arg:
            arglen = len(arg)
            if arglen > lengthOfLongestLine:
                lengthOfLongestLine = arglen


#    normalprint("")
    normalprint("-"*(lengthOfLongestLine+4))
    normalprint("| " + text + " "*(lengthOfLongestLine - len(text)) + " |")
    for arg in args:
        for arg in arg:
            normalprint("| " + arg + " "*(lengthOfLongestLine - len(arg)) + " |")
    normalprint("-"*(lengthOfLongestLine+4))
#    normalprint("")


# print("Überschrift", *["liste", "von", "argumenten", str(1)])