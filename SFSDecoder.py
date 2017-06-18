from struct import unpack
from SFSObject import SFSObject
from SFSType import sfx_types_order, sfx_support_types

class SFSDecoder:
    def __init__(self, buff):
        self.__idx = 0
        self.__buffer = buff

    def _get(self, length):
        self.__idx += length
        if self.__idx >= len(self.__buffer) + 1:
            raise Exception("get length " + str(length) + " from " + str(self.__idx) + " out of range")

        return self.__buffer[self.__idx - length: self.__idx]

    def _getByte(self):
        return unpack('b', self._get(1))[0]

    def _getShort(self):
        return unpack('!h', self._get(2))[0]

    def _getInt(self):
        return unpack('!i', self._get(4))[0]

    def _getLong(self):
        return unpack('!q', self._get(8))[0]

    def _getFloat(self):
        return unpack('!f', self._get(4))[0]

    def _getDouble(self):
        return unpack('!d', self._get(8))[0]

    def _getString(self):
        return self._get(self._getShort()).decode('utf-8')

    def _getObjectType(self):
        objtype = self._getByte()
        if objtype >= len(sfx_types_order):
            return "unknown object type"
        return sfx_types_order[objtype]

    def _getArray(self, basetype):
        arr = []
        arrSize = self._getShort()
        objdecoder = sfx_support_types[basetype]['decoder']

        for n in range(0, arrSize):
            val = objdecoder(self)
            arr.append(val)

        return arr

    def _getObjAndType(self):
        objtype = self._getObjectType()
        if objtype not in sfx_support_types:
            raise Exception("unsupport object type: " + objtype)
        objdecoder = sfx_support_types[objtype]['decoder']
        obj = objdecoder(self)
        return (objtype, obj)

    def _getSFXArray(self):
        arr = []
        arrSize = self._getShort()

        for n in range(0, arrSize):
            val = self._getObjAndType()
            arr.append(val)

        return arr

    def _getSFXObject(self):
        sfsObj = SFSObject()
        dataSize = self._getShort()
        for n in range(0, dataSize):
            key = self._getString()
            val = self._getObjAndType()
            sfsObj.add_orign_object(key, val)
        return sfsObj

    def getSFSObject(self):
        if self._getObjectType() != "object":
            return "this is not an object"
        return self._getSFXObject()



