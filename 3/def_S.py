#def_S.py
S_table_enc ={
    0b000 : 0b101,
    0b001 : 0b011,
    0b010 : 0b100,
    0b011 : 0b110,
    0b100 : 0b010,
    0b101 : 0b111,
    0b110 : 0b000,
    0b111 : 0b001
}

S_table_dec ={
    0b101: 0b000,
    0b011: 0b001,
    0b100: 0b010,
    0b110: 0b011,
    0b010: 0b100,
    0b111: 0b101,
    0b000: 0b110,
    0b001: 0b111
}

def S_enc(input):
    ret_enc = bin(S_table_enc[input])[2:].zfill(3)
    bin_ret_enc = int(ret_enc,2)
    return bin_ret_enc