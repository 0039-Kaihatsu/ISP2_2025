# Attack_1.py
# include time
import def_S_1 # type: ignore
from Encrypt_1 import encrypt_pt_1 # type: ignore
import time

def zero_bin(x, w):
    return bin(x)[2:].zfill(w)

def candidates_for_pair_using_dec(pt, ct, s_table_dec):
    key_can = []
    for key in range(4):
        k1 = (key >> 1) & 0b1
        k2 = key & 0b1
        v2 = ct ^ k2
        v1 = s_table_dec[v2]
        if (v1 ^ k1) == pt:
            key_can.append(key)
    return key_can

def early_end():
    early_end = input("早期終了あり(y) or なし(n)")
    return early_end

def main():
    s_table_dec = def_S_1.S_table_dec_1

    all_candidates = None

    ee = early_end()

    s_time = float(time.time())

    for pt in range(2):
        ct = encrypt_pt_1(pt)  
        # print(f"平文 {zero_bin(pt,1)} -> 暗号文 {zero_bin(ct,1)}")

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
                print(f" 決定候補: key={zero_bin(k,2)}  key1={zero_bin((k>>1)&0b1,1)}  key2={zero_bin(k&0b1,1)}")
                break
        else:
            continue

    e_time = float(time.time())
    print("=== 処理終了 ===")
    if all_candidates:
        if len(all_candidates) > 1:
            print(f"最終的な共通候補鍵数: {len(all_candidates)}")
            for k in sorted(all_candidates):
                print(f" key={zero_bin(k,2)}  key1={zero_bin((k>>1)&0b1,1)} key2={zero_bin(k&0b1,1)}")
    else:
        print("共通候補は存在しませんでした。")
    
    print(f"処理時間{e_time - s_time}")

if __name__ == '__main__':
    main()
