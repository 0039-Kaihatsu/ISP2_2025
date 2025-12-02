# Encrypt_12.py
import def_S_12   # type: ignore

reference_key = 0b111111111100000000001111

def encrypt_pt_12(pt, use_key=None):
    if use_key is None:
        key = reference_key
    else:
        key = use_key
    key1 = (key >> 12) & 0b111111111111
    key2 = key & 0b111111111111
    Ct1 = pt ^ key1
    Ct2 = def_S_12.S_enc(Ct1)
    Ct3 = Ct2 ^ key2
    return Ct3