S_table_enc_2 = {
    0b00 : 0b10,
    0b01 : 0b01,
    0b10 : 0b11,
    0b11 : 0b00,
}

S_table_dec_2 = {v: k for k, v in S_table_enc_2.items()}

def S_enc(input):
    ret_enc = bin(S_table_enc_2[input])[2:].zfill(10)
    bin_ret_enc = int(ret_enc,2)
    return bin_ret_enc