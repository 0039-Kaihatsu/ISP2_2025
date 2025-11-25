# Encrypt.py
import def_S

reference_key = 0b110100

def encrypt_pt(pt, use_key=None):
    if use_key is None:
        key = reference_key
    else:
        key = use_key
    key1 = (key >> 3) & 0b111
    key2 = key & 0b111
    Ct1 = pt ^ key1
    Ct2 = def_S.S_enc(Ct1)
    Ct3 = Ct2 ^ key2
    return Ct3
