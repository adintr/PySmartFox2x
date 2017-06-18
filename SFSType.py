sfx_support_types = {
    "null": {
        'id': 0,
        'decoder': lambda coder: None,
        'encoder': lambda coder, obj : None,
    },
    "bool": {
        'id': 1,
        'decoder': lambda coder: coder._getByte() == 1,
        'encoder': lambda coder, obj: coder._putbyte(obj and 1 or 0),
    },
    "byte": {
        'id': 2,
        'decoder': lambda coder: coder._getByte(),
        'encoder': lambda coder, obj: coder._putbyte(obj),
    },
    "short": {
        'id': 3,
        'decoder': lambda coder: coder._getShort(),
        'encoder': lambda coder, obj: coder._putshort(obj),
    },
    "int": {
        'id': 4,
        'decoder': lambda coder: coder._getInt(),
        'encoder': lambda coder, obj: coder._putint(obj),
    },
    "long": {
        'id': 5,
        'decoder': lambda coder: coder._getLong(),
        'encoder': lambda coder, obj: coder._putlong(obj),
    },
    "float": {
        'id': 6,
        'decoder': lambda coder: coder._getFloat(),
        'encoder': lambda coder, obj: coder._putfloat(obj),
    },
    "double": {
        'id': 7,
        'decoder': lambda coder: coder._getDouble(),
        'encoder': lambda coder, obj: coder._putdouble(obj),
    },
    "string": {
        'id': 8,
        'decoder': lambda coder: coder._getString(),
        'encoder': lambda coder, obj: coder._putstring(obj),
    },
    "object": {
        'id': 18,
        'decoder': lambda coder: coder._getSFXObject(),
        'encoder': lambda coder, obj: coder._putobject(obj),
    },
    "bool_array": {
        'id': 9,
        'decoder': lambda coder: coder._getArray('bool'),
        'encoder': lambda coder, obj: coder._putarray(obj, 'bool'),
    },
    "byte_array": {
        'id': 10,
        'decoder': lambda coder: coder._getArray('byte'),
        'encoder': lambda coder, obj: coder._putarray(obj, 'byte'),
    },
    "short_array": {
        'id': 11,
        'decoder': lambda coder: coder._getArray('short'),
        'encoder': lambda coder, obj: coder._putarray(obj, 'short'),
    },
    "int_array": {
        'id': 12,
        'decoder': lambda coder: coder._getArray('int'),
        'encoder': lambda coder, obj: coder._putarray(obj, 'int'),
    },
    "long_array": {
        'id': 13,
        'decoder': lambda coder: coder._getArray('long'),
        'encoder': lambda coder, obj: coder._putarray(obj, 'long'),
    },
    "float_array": {
        'id': 14,
        'decoder': lambda coder: coder._getArray('float'),
        'encoder': lambda coder, obj: coder._putarray(obj, 'float'),
    },
    "double_array": {
        'id': 15,
        'decoder': lambda coder: coder._getArray('double'),
        'encoder': lambda coder, obj: coder._putarray(obj, 'double'),
    },
    "string_array": {
        'id': 16,
        'decoder': lambda coder: coder._getArray('string'),
        'encoder': lambda coder, obj: coder._putarray(obj, 'string'),
    },
    "sfxobj_array": {
        'id': 17,
        'decoder': lambda coder: coder._getSFXArray(),
        'encoder': lambda coder, obj: coder._putSFXObjArray(obj),
    },
}

sfx_types_order = [
    "null",         # 0
    "bool",         # 1
    "byte",         # 2
    "short",        # 3
    "int",          # 4
    "long",         # 5
    "float",        # 6
    "double",       # 7
    "string",       # 8
    "bool_array",   # 9
    "byte_array",   # 10
    "short_array",  # 11
    "int_array",    # 12
    "long_array",   # 13
    "float_array",  # 14
    "double_array", # 15
    "string_array", # 16
    "sfxobj_array", # 17
    "object",       # 18
    "class",        # 19
]
