import socket
from SFSEncoder import object2binary
from SFSDecoder import decodeObject, SFSBuffer
from HelpFunc import printByteArray

class SF2XClient:
    def __init__(self, addr, port, debugMode = True):
        self.addr = addr
        self.port = port
        self.debug = debugMode
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.sock.connect((self.addr, self.port))

    def request(self, sfxobject, controller = 0, msgid = 0):
        sendobj = {
            'c': ('byte', controller),
            'a': ('short', msgid),
            'p': ('object', sfxobject),
        }

        stream = bytearray()
        packet = object2binary(sendobj)
        stream.append(8*16)
        stream.append((len(packet)/256)%256)
        stream.append(len(packet)%256)
        stream.extend(packet)

        self.sock.send(stream)

        header = self.sock.recv(3)
        dataLen = ord(header[1]) * 256 + ord(header[2])

        if self.debug:
            print 'recv data len:' + str(dataLen)

        recv_len = 0
        data = bytearray()
        while recv_len < dataLen:
            r = self.sock.recv(dataLen - recv_len)
            data.extend(r)
            recv_len += len(r)

        if self.debug:
            printByteArray(data)

        return decodeObject(SFSBuffer(data))
