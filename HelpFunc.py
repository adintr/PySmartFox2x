import re
from SFSDecoder import decodeObject, SFSBuffer

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

# UseAge: analyzePack("12 00 03 00 01 61 03 00 00 00 01 63 02 00 00 01 70 12 00 03 00 03 62 69 6E 01 01 00 02 63 6C 08 00 07 41 6E 64 72 6F 69 64 00 03 61 70 69 08 00 05 31 2E 36 2E 31")
def analyzePack(strhex):
    packdata = readByteArray(strhex)
    printByteArray(packdata)
    print decodeObject(SFSBuffer(packdata))[1]