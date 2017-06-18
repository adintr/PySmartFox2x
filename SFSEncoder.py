from SFSObject import SFSObject
from SFSType import sfx_support_types
from struct import pack

class SFSEncoder:
    def __init__(self):
        self.buff = bytearray()

    def encodeObject(self, sfsobject):
        self._putbyte(self._get_type_id("object"))
        self._putobject(sfsobject)
        return self.buff

    def _get_type_id(self, typename):
        if typename not in sfx_support_types:
            raise Exception("unsupport type: " + typename)
        return sfx_support_types[typename]['id']

    def _putbyte(self, byte):
        self.buff.append(byte)

    def _putbytes(self, bytes):
        self.buff.extend(bytes)

    def _putshort(self, val):
        self._putbytes(pack('!h', val))

    def _putint(self, val):
        self._putbytes(pack('!i', val))

    def _putlong(self, val):
        self._putbytes(pack('!q', val))

    def _putfloat(self, val):
        self._putbytes(pack('!f', val))

    def _putdouble(self, val):
        self._putbytes(pack('!d', val))

    def _putstring(self, val):
        strbyte = bytearray(unicode(val).encode('utf-8'))
        self._putshort(len(strbyte))
        self._putbytes(strbyte)

    def _putobject(self, object):
        if isinstance(object, SFSObject):
            object = object.get_origin_objects()

        obj_len = len(object)
        self._putshort(obj_len)

        for key in object:
            self._putstring(key)
            objtype = object[key][0]
            objval = object[key][1]

            self._putbyte(self._get_type_id(objtype))
            encoder = sfx_support_types[objtype]['encoder']
            encoder(self, objval)

    def _putarray(self, objects, basetype):
        encoder = sfx_support_types[basetype]['encoder']
        objlen = len(objects)
        self._putshort(objlen)

        for i in range(0, objlen):
            obj = objects[i]
            encoder(self, obj)

    def _putSFXObjArray(self, objects):
        objlen = len(objects)
        self._putshort(objlen)

        for i in range(0, objlen):
            objtype = objects[i][0]
            objval = objects[i][1]
            self._putbyte(self._get_type_id(objtype))
            encoder = sfx_support_types[objtype]['encoder']
            encoder(self, objval)

def encode_sfx_object(sfsobj):
    encoder = SFSEncoder()
    return encoder.encodeObject(sfsobj)