import re

def printByteArray(data):
    shtr = str(data).encode('hex')
    shtr = re.sub(r"(\w{32})", "\\1\n", shtr)
    shtr = re.sub(r"(\w\w)", "\\1 ", shtr)
    print shtr

def readByteArray(str):
    str = str.replace(' ', '')
    str = str.replace('\n', '')
    str = str.replace('\r', '')
    str = str.replace('\t', '')
    return bytearray(str.decode('hex'))