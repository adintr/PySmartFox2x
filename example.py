from xlibs.smartfox2x.SFSClient import SF2XClient
from xlibs.smartfox2x.SFSObject import SFSObject

def te_st1():
    from xlibs.smartfox2x.HelpFunc import analyzePack
    analyzePack("""
        12 00 03 00 01 61 03 00 02 00 01 70 12 00 03 00 
        01 70 12 00 04 00 08 70 6c 61 79 65 72 49 64 08 
        00 01 31 00 07 74 72 61 64 65 4e 6f 08 00 08 30 
        30 30 31 30 30 30 30 00 0a 6d 6f 6e 65 79 43 6f 
        75 6e 74 04 00 00 00 64 00 04 73 69 67 6e 08 00 
        20 37 31 63 39 61 65 61 38 36 62 37 34 39 36 65 
        30 31 33 35 64 61 36 63 33 34 64 32 33 64 38 65 
        64 00 01 63 08 00 0c 55 73 65 72 52 65 63 68 61 
        72 67 65 00 01 72 04 ff ff ff ff 00 01 63 02 00
        """)

def te_st2():
    sfxc = SF2XClient('52.29.112.144', 9933, True)
    sfxc.connect()
    if not sfxc.login('username', 'password', 'china', {'myarg': ('int', 1)}):
        print "login failed!"
        return False

    print "login success!"

    charge_obj = SFSObject()
    charge_obj.put_string("player", 1)
    charge_obj.put_string("trade", 2)
    charge_obj.put_int("money", 3)

    res = sfxc.extension_request("Recharge", charge_obj)
    if res['p']['p']['success']:
        print "charge success!"
    else:
        errmsg = res['p']['p']['errmsg']
        print "charge failed: " + errmsg

if __name__ == "__main__":
    te_st1()
    te_st2()


