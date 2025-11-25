# Encrypt_1.py
import def_S_1 # type: ignore

reference_key = 0b10

def encrypt_pt_1(pt, use_key=None):
    if use_key is None:
        key = reference_key
    else:
        key = use_key
    key1 = (key >> 1) & 0b1
    key2 = key & 0b1
    Ct1 = pt ^ key1
    Ct2 = def_S_1.S_enc(Ct1)
    Ct3 = Ct2 ^ key2
    return Ct3
