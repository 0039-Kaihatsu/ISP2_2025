import random

def generate_sbox(n_bits, seed=None):
    """nビットの全単射S-box（1対1対応）を生成"""
    if seed is not None:
        random.seed(seed)
    
    size = 2 ** n_bits
    inputs = list(range(size))
    outputs = inputs.copy()
    random.shuffle(outputs)
    
    sbox = {i: outputs[i] for i in range(size)}
    return sbox


# --- S-boxを生成 ---
n = 9

S_table_enc = generate_sbox(n, seed=42)

# --- Pythonファイルに保存 ---
filename = f"def_S_{n}.py"

with open(filename, "w", encoding="utf-8") as f:
    f.write(f"S_table_enc_{n} = {{\n")
    for k, v in sorted(S_table_enc.items()):
        f.write(f"    0b{k:0{n}b} : 0b{v:0{n}b},\n")
    f.write("}\n")

print(f"{filename} に S_table_enc_{n}（2進数表記）を出力しました。")
