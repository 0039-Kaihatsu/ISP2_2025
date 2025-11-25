# Encrypt_11.py
import def_S_11   # type: ignore

reference_key = 0b0000000000111111111100

def encrypt_pt_11(pt, use_key=None):
    if use_key is None:
        key = reference_key
    else:
        key = use_key
    key1 = (key >> 11) & 0b11111111111
    key2 = key & 0b11111111111
    Ct1 = pt ^ key1
    Ct2 = def_S_11.S_enc(Ct1)
    Ct3 = Ct2 ^ key2
    return Ct3