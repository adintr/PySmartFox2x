from SFSType import sfx_support_types

class SFSObject:
    def __init__(self, origobject = None):
        self.object = origobject
        if(self.object is None):
            self.object = {}

    def __unicode__(self):
        return self.show_object(0)

    def __str__(self):
        return self.show_object(0)

    def put_string(self, name, val):
        self.add_object(name, "string", str(val))

    def put_int(self, name, val):
        self.add_object(name, "int", int(val))

    def add_orign_object(self, name, typeobj):
        if len(typeobj) != 2:
            raise Exception("typeobject should be (type, obj) format")

        if typeobj[0] not in sfx_support_types:
            raise Exception("the type " + typeobj[0] + " is not support now")

        self.object[name] = typeobj

    def add_object(self, name, type, object):
        self.object[name] = (type, object)

    def to_pyobject(self):
        robj = {}
        for key in self.object:
            objtype = self.object[key][0]
            objval = self.object[key][1]
            if objtype == "object":
                robj[key] = objval.to_pyobject()
            else:
                robj[key] = objval
        return robj

    def show_object(self, indent):
        retstr = "<object> {\n"
        indent += 1
        for key in self.object:
            retstr += "\t" * indent + key + ": "
            retstr += self.show_object_by_type(self.object[key][0], self.object[key][1], indent)
            retstr += "\n"
        retstr += "\t" * (indent - 1) + "}"
        return retstr

    def get_origin_objects(self):
        return self.object

    def show_object_by_type(self, type, obj, indent):
        if type == "object":
            return obj.show_object(indent)

        if type in ("bool", "byte", "short", "int", "long", "float", "double", "string"):
            return unicode(obj) + " <" + type + ">"

        if type == "sfxobj_array":
            retstr = "<sfx_array> [\n"
            for i in range(0, len(obj)):
                retstr += "\t" * (indent + 1) + str(i) + ": "
                retstr += self.show_object_by_type(obj[i][0], obj[i][1], indent + 1)
                retstr += "\n"
            retstr += "\t" * (indent) + "]"
            return retstr

        if type in ("byte_array", "bool_array", "short_array", "int_array", "long_array", "float_array", "double_array", "string_array", ):
            retstr = "<" + type + "> [\n"
            basetype = type[0:-6]
            for i in range(0, len(obj)):
                retstr += "\t" * (indent + 1) + str(i) + ": "
                retstr += self.show_object_by_type(basetype, obj[i], indent + 1)
                retstr += "\n"
            retstr += "\t" * (indent) + "]"
            return retstr

        return type
