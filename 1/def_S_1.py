S_table_enc_1 = {
    0b0 : 0b1,
    0b1 : 0b0,
}

S_table_dec_1 = {v: k for k, v in S_table_enc_1.items()}

def S_enc(input):
    ret_enc = bin(S_table_enc_1[input])[2:].zfill(10)
    bin_ret_enc = int(ret_enc,2)
    return bin_ret_enc
