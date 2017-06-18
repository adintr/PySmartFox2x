sfx_support_types = {
    "null": {
        'decoder': lambda coder: None,
    },
    "bool": {
        'decoder': lambda coder: coder._getByte() == 1,
    },
    "byte": {
        'decoder': lambda coder: coder._getByte(),
    },
    "short": {
        'decoder': lambda coder: coder._getShort(),
    },
    "int": {
        'decoder': lambda coder: coder._getInt(),
    },
    "long": {
        'decoder': lambda coder: coder._getLong(),
    },
    "float": {
        'decoder': lambda coder: coder._getFloat(),
    },
    "double": {
        'decoder': lambda coder: coder._getDouble(),
    },
    "string": {
        'decoder': lambda coder: coder._getString(),
    },
    "object": {
        'decoder': lambda coder: coder._getSFXObject(),
    },
    "bool_array": {
        'decoder': lambda coder: coder._getArray('bool'),
    },
    "byte_array": {
        'decoder': lambda coder: coder._getArray('byte'),
    },
    "short_array": {
        'decoder': lambda coder: coder._getArray('short'),
    },
    "int_array": {
        'decoder': lambda coder: coder._getArray('int'),
    },
    "long_array": {
        'decoder': lambda coder: coder._getArray('long'),
    },
    "float_array": {
        'decoder': lambda coder: coder._getArray('float'),
    },
    "double_array": {
        'decoder': lambda coder: coder._getArray('double'),
    },
    "string_array": {
        'decoder': lambda coder: coder._getArray('string'),
    },
    "sfxobj_array": {
        'decoder': lambda coder: coder._getObjAndType(),
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
