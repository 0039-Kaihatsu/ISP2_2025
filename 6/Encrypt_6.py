# Encrypt_6.py
import def_S_6 # type: ignore

reference_key = 0b111111000000 #変更

def encrypt_pt_6(pt, use_key=None):
    if use_key is None:
        key = reference_key
    else:
        key = use_key
    key1 = (key >> 6) & 0b111111 #変更
    key2 = key & 0b111111 #変更
    Ct1 = pt ^ key1
    Ct2 = def_S_6.S_enc(Ct1) #変更
    Ct3 = Ct2 ^ key2
    return Ct3