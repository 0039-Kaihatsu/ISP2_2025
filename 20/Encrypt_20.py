# Encrypt_20.py
import def_S_20  # pyright: ignore[reportMissingImports]

reference_key = 0b001011101010100110101010111001011011001

def encrypt_pt_20(pt, use_key=None):
    if use_key is None:
        key = reference_key
    else:
        key = use_key
    key1 = (key >> 20) & 0b11111111111111111111
    key2 = key & 0b11111111111111111111
    Ct1 = pt ^ key1
    Ct2 = def_S_20.S_enc(Ct1)
    Ct3 = Ct2 ^ key2
    return Ct3
