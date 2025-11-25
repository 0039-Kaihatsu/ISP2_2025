# Attack_20.py
# include time
import def_S_20 # pyright: ignore[reportMissingImports]
from Encrypt_20 import encrypt_pt_20 # pyright: ignore[reportMissingImports]
import time

def zero_bin(x, w):
    return bin(x)[2:].zfill(w)

def candidates_for_pair_using_dec(pt, ct, s_table_dec):
    key_can = []
    for key in range(2**40):
        k1 = (key >> 20) & 0b11111111111111111111
        k2 = key & 0b11111111111111111111
        v2 = ct ^ k2
        v1 = s_table_dec[v2]
        if (v1 ^ k1) == pt:
            key_can.append(key)
    return key_can

def early_end():
    early_end = input("早期終了あり(y) or なし(n)")
    return early_end

def main():
    s_table_dec = def_S_20.S_table_dec_20

    all_candidates = None

    ee = early_end()

    s_time = float(time.time())

    for pt in range(2**20):
        ct = encrypt_pt_20(pt)  
        # print(f"平文 {zero_bin(pt,20)} -> 暗号文 {zero_bin(ct,20)}")

        key_can = candidates_for_pair_using_dec(pt, ct, s_table_dec)
        # print(f"  この平文単独の候補鍵数: {len(key_can)}")

        if all_candidates is None:
            all_candidates = set(key_can)
        else:
            all_candidates &= set(key_can)

        # print(f"  これまでの共通候補数: {len(all_candidates)}\n")

        if ee == "y":
            # 早期終了条件
            if not all_candidates:
                print("候補が0になったため中断します（実装やテーブルを確認してください）。")
                break
            if len(all_candidates) == 1:
                k = next(iter(all_candidates))
                print("候補が1つに絞られました。早期終了します。")
                print(f" 決定候補: key={zero_bin(k,40)}  key1={zero_bin((k>>20)&0b11111111111111111111,20)}  key2={zero_bin(k&0b11111111111111111111,20)}")
                break
        else:
            continue

    e_time = float(time.time())
    print("=== 処理終了 ===")
    if all_candidates:
        if len(all_candidates) > 1:
            print(f"最終的な共通候補鍵数: {len(all_candidates)}")
            for k in sorted(all_candidates):
                print(f" key={zero_bin(k,40)}  key1={zero_bin((k>>20)&0b11111111111111111111,20)} key2={zero_bin(k&0b11111111111111111111,20)}")
    else:
        print("共通候補は存在しませんでした。")
    
    print(f"処理時間{e_time - s_time}")

if __name__ == '__main__':
    main()
