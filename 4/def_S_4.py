S_table_enc_4 = {
    0b0000 : 0b0111,
    0b0001 : 0b1001,
    0b0010 : 0b0101,
    0b0011 : 0b0110,
    0b0100 : 0b1110,
    0b0101 : 0b1010,
    0b0110 : 0b1100,
    0b0111 : 0b1000,
    0b1000 : 0b0001,
    0b1001 : 0b0010,
    0b1010 : 0b1101,
    0b1011 : 0b1111,
    0b1100 : 0b0100,
    0b1101 : 0b1011,
    0b1110 : 0b0000,
    0b1111 : 0b0011,
}

#def_Sの最後に追加

S_table_dec_4 = {v: k for k, v in S_table_enc_4.items()} #変更

def S_enc(input):
    ret_enc = bin(S_table_enc_4[input])[2:].zfill(10) #変更
    bin_ret_enc = int(ret_enc,2)
    return bin_ret_enc