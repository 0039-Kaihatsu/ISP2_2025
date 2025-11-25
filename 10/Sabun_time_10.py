#Sabun_time.py
import def_S_10 # type: ignore
import Encrypt_10 # type: ignore
import time

# 3桁の2進数にするもの
def zb(x, w):
    return format(x, 'b').zfill(w)

# (下から)S(ct⊕k2)⊕k1=ptを行っている
def candidates_for_pair_using_dec(pt, ct,s_table_dec):
    key_can = []
    for key in range(4**10):
        k1 = (key >> 10) & 0b1111111111
        k2 = key & 0b1111111111
        v2 = ct ^ k2
        if v2 not in s_table_dec:
            continue
        v1 = s_table_dec[v2]
        if (v1 ^ k1) == pt:
            key_can.append(key)
    return key_can

#c1⊕c2を求める
def differential_filter_k1(pairs):
    deltas_c = {}
    n = len(pairs)
    for i in range(n):
        for j in range(i+1, n):#range(start,stop(未満))
            deltas_c[(i, j)] = pairs[i][1] ^ pairs[j][1]

#k1を求める
    k1_candidates = []
    for k1 in range(2**10):
        ok = True
        for (i, j), dC in deltas_c.items():
            p_i, c_i = pairs[i]
            p_j, c_j = pairs[j]
            x_i = p_i ^ k1
            x_j = p_j ^ k1
            s_xi = def_S_10.S_enc(x_i)
            s_xj = def_S_10.S_enc(x_j)
            if (s_xi ^ s_xj) != dC:
                ok = False
                break
        if ok:
            k1_candidates.append(k1)
    return k1_candidates

# --- k1 候補から k2 を復元し、全ペアで検証する
def recover_keys_from_k1_candidates(k1_list, pairs):
    keys = []
    for k1 in k1_list:
        p0, c0 = pairs[0]
        k2 = def_S_10.S_enc(p0 ^ k1) ^ c0
        key = (k1 << 10) | k2 #上位10ビットが k1、下位10ビットが k2 になる20ビット鍵を作る
        ok = True
        for p, c in pairs:
            if Encrypt_10.encrypt_pt_10(p, use_key=key) != c:
                ok = False
                break
        if ok:
            keys.append((key, k1, k2))
    return keys

# 3桁の二進数すべてを平文として暗号化したもの
def main():
    pairs = []
    s_time = float(time.time())
    for i in range(2**10):
        pairs.append((i,Encrypt_10.encrypt_pt_10(i)))
    
    # print("pairs の中身:")
    # for p, c in pairs:
    #     print(f"平文: {zb(p,3)}, 暗号文: {zb(c,3)}")



    # print("参照鍵で平文 0..7 を暗号化した対応表：")
    # for pt in range(1024):
    #     print(f" 平文 P={zb(pt,10)} -> 暗号 C={zb(Encrypt_10.encrypt_pt_10(pt),10)}")

    # print("\n攻撃に用いる平文-暗号文ペア：")
    # for i, (p, c) in enumerate(pairs, start=1):
    #     print(f" P{i} = {zb(p,10)}  ,  C{i} = {zb(c,10)}")
    

    
    # # 各ペアごとの候補を列挙
    # print("\n各平文-暗号文ペア単独で成立する鍵候補（復号テーブル法）:")
    # per_pair_candidates = []
    # for idx, (p, c) in enumerate(pairs, start=1):
    #     candidate = candidates_for_pair_using_dec(p, c,def_S_10.S_table_dec_10)
    #     per_pair_candidates.append(set(candidate))
    #     print(f" ペア{idx}: 候補数 = {len(candidate)} -> {[zb(k,20) for k in sorted(candidate)]}")

    # # 全ペアの共通候補
    # common = set.intersection(*per_pair_candidates)
    # print(f"\n全てのペアを同時に満たす鍵の共通集合: {len(common)} 個")
    # for k in sorted(common):
    #     print(" 鍵 =", zb(k,20), " 上位(k1) =", zb((k>>10)&0b1111111111,10), " 下位(k2) =", zb(k&0b1111111111,10))

    # # 差分フィルタで k1 を絞る
    k1_candidates = differential_filter_k1(pairs)
    # print("\n差分フィルタによって残った k1 の候補一覧：", [zb(x,3) for x in k1_candidates])

    # k1 から鍵復元して全ペア検証
    recovered = recover_keys_from_k1_candidates(k1_candidates, pairs)
    print("\nk1 候補から復元し、すべてのペアで検証して残った鍵：")
    if recovered:
        for key_val, k1, k2 in recovered:
            print(f" 鍵 = {zb(key_val,20)}  (k1={zb(k1,10)}, k2={zb(k2,10)})")
    else:
        print(" どの k1 でも全ペアを同時に満たす鍵は見つかりませんでした。")
    e_time = float(time.time())

    print(f"処理時間{e_time - s_time}")

    # # 最後に全鍵空間での検証（保険）
    # all_ok = []
    # for k in range(64):
    #     good = True
    #     for p, c in pairs:
    #         if Encrypt.encrypt_pt(p, use_key=k) != c:
    #             good = False
    #             break
    #     if good:
    #         all_ok.append(k)
    # print("\n全鍵空間（0..63）を走査して見つかった鍵（検算）:", [zb(k,6) for k in all_ok])

if __name__ == '__main__':
    main()