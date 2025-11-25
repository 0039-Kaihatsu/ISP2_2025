# Encrypt_2.py
import def_S_2 # type: ignore

reference_key = 0b1100 #変更

def encrypt_pt_2(pt, use_key=None):
    if use_key is None:
        key = reference_key
    else:
        key = use_key
    key1 = (key >> 2) & 0b11 #変更
    key2 = key & 0b11 #変更
    Ct1 = pt ^ key1
    Ct2 = def_S_2.S_enc(Ct1) #変更
    Ct3 = Ct2 ^ key2
    return Ct3
