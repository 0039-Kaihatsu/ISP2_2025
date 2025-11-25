# Encrypt_4.py
import def_S_4 # type: ignore

reference_key = 0b11110000 #変更

def encrypt_pt_4(pt, use_key=None):
    if use_key is None:
        key = reference_key
    else:
        key = use_key
    key1 = (key >> 4) & 0b1111 #変更
    key2 = key & 0b1111 #変更
    Ct1 = pt ^ key1
    Ct2 = def_S_4.S_enc(Ct1) #変更
    Ct3 = Ct2 ^ key2
    return Ct3