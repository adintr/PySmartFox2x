import socket, hashlib
from SFSEncoder import object2binary
from SFSDecoder import SFSDecoder
from HelpFunc import printByteArray

class SF2XClient:
    def __init__(self, addr, port, debugMode = True):
        self.addr = addr
        self.port = port
        self.debug = debugMode
        self.msgid = 0
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.sock.connect((self.addr, self.port))
        res = self.request({'bin': ('bool', True), 'api': ('string', '1.6.1'), 'cl': ('string', 'Android')})
        self.token = res['p']['tk']
        if self.debug:
            print "Connect Token: ", self.token

    def login(self, username, password, zone, extobj):
        if not self.token:
            return False

        md5 = hashlib.md5()
        md5.update(self.token + password)
        sfxpass = md5.hexdigest()

        loginObj = {
            'zn': ('string', zone),
            'un': ('string', username),
            'pw': ('string', sfxpass),
            'p': ('object', extobj),
        }

        res = self.request(loginObj)
        resp = res['p']
        if 'ec' in resp:
            return False

        if 'rs' in resp:
            return True

        return False

    def extension_request(self, cmd, sfxobject, roomid = -1):
        extobject = {
            'c': ('string', cmd),
            'r': ('int', roomid),
            'p': ('object', sfxobject),
        }
        return self.request(extobject, 1)

    def request(self, sfxobject, controller = 0):
        sendobj = {
            'c': ('byte', controller),
            'a': ('short', self.msgid),
            'p': ('object', sfxobject),
        }

        self.msgid += 1
        stream = bytearray()
        packet = object2binary(sendobj)
        sendLen = len(packet)
        stream.append(8 * 16)
        stream.append((sendLen / 256) % 256)
        stream.append(sendLen % 256)
        stream.extend(packet)

        if self.debug:
            print "send object: ", sendobj
            print "send data len: ", sendLen
            printByteArray(packet)
            print "\n"

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

        resobj = SFSDecoder(data).getSFSObject()
        if self.debug:
            print "Decode: ", unicode(resobj)
            print "\n"

        return resobj.to_pyobject()
