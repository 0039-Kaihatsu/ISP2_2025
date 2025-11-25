# Encrypt_10.py
import def_S_10   # type: ignore

reference_key = 0b00000111111111100000

def encrypt_pt_10(pt, use_key=None):
    if use_key is None:
        key = reference_key
    else:
        key = use_key
    key1 = (key >> 10) & 0b1111111111
    key2 = key & 0b1111111111
    Ct1 = pt ^ key1
    Ct2 = def_S_10.S_enc(Ct1)
    Ct3 = Ct2 ^ key2
    return Ct3
