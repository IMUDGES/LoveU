import hashlib

def encrypt(str):
    m = hashlib.md5()
    m.update(str)
    psw = m.hexdigest()
    return psw