

class SFSObject:
    __support_types = {
        "null": None,
        "bool": None,
        "byte": None,
        "short": None,
        "int": None,
        "long": None,
        "float": None,
        "double": None,
        "string": None,
        "object": None,
        "byte_array": None,
        "int_array": None,
        "long_array": None,
        "float_array": None,
        "double_array": None,
        "string_array": None,
        "array_array": None,
        "object_array": None,
    }

    def __init__(self):
        self.object = {}

    def __unicode__(self):
        return self.show_object(0)

    def __str__(self):
        return self.show_object(0)

    def add_orign_object(self, name, typeobj):
        if len(typeobj) != 2:
            raise Exception("typeobject should be (type, obj) format")

        if typeobj[0] not in SFSObject.__support_types:
            raise Exception("the type " + typeobj[0] + " is not support now")

        self.object[name] = typeobj

    def show_object(self, indent):
        retstr = "<object> {\n"
        indent += 1
        for key in self.object:
            retstr += "\t" * indent + key + ": "
            retstr += self.show_object_by_type(self.object[key][0], self.object[key][1], indent)
            retstr += "\n"
        retstr += "\t" * (indent - 1) + "}"
        return retstr

    def show_object_by_type(self, type, obj, indent):
        if type == "object":
            return obj.show_object(indent)

        if type in ("bool", "byte", "short", "int", "long", "float", "double", "string"):
            return str(obj) + " <" + type + ">"

        if type in ("byte_array", "int_array", "long_array", "float_array", "double_array", "string_array", "array_array", "object_array"):
            retstr = "<" + type + "> [\n"
            basetype = type[0:-6]
            for i in range(0, len(obj)):
                retstr += "\t" * (indent + 1) + str(i) + ": "
                retstr += self.show_object_by_type(basetype, obj[i], indent + 1)
                retstr += "\n"
            retstr += "\t" * (indent) + "]"
            return retstr

        return type
