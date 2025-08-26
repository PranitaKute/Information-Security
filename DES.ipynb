# Permutation Tables (same as before)
# ----------------------
IP = [58,50,42,34,26,18,10,2,60,52,44,36,28,20,12,4,62,54,46,38,30,22,14,6,64,56,48,40,32,24,16,8,
      57,49,41,33,25,17,9,1,59,51,43,35,27,19,11,3,61,53,45,37,29,21,13,5,63,55,47,39,31,23,15,7]
FP = [40,8,48,16,56,24,64,32,39,7,47,15,55,23,63,31,38,6,46,14,54,22,62,30,37,5,45,13,53,21,61,29,
      36,4,44,12,52,20,60,28,35,3,43,11,51,19,59,27,34,2,42,10,50,18,58,26,33,1,41,9,49,17,57,25]
E = [32,1,2,3,4,5,4,5,6,7,8,9,8,9,10,11,12,13,12,13,14,15,16,17,16,17,18,19,20,21,20,21,22,23,24,25,24,25,26,27,28,29,28,29,30,31,32,1]
P = [16,7,20,21,29,12,28,17,1,15,23,26,5,18,31,10,2,8,24,14,32,27,3,9,19,13,30,6,22,11,4,25]

S_BOX = [
  # S1
  [[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],
   [0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],
   [4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],
   [15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]],
  # S2
  [[15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],
   [3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],
   [0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],
   [13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]],
  # S3
  [[10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],
   [13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],
   [13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],
   [1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]],
  # S4
  [[7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],
   [13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],
   [10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],
   [3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]],
  # S5
  [[2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],
   [14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],
   [4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],
   [11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]],
  # S6
  [[12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],
   [10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],
   [9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],
   [4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]],
  # S7
  [[4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],
   [13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],
   [1,4,11,13,12,3,7,14,10,15,6,8,0,9,2,5],
   [6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]],
  # S8
  [[13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],
   [1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],
   [7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],
   [2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]]
]

PC1 = [57,49,41,33,25,17,9,1,58,50,42,34,26,18,10,2,59,51,43,35,27,19,11,3,60,52,44,36,
       63,55,47,39,31,23,15,7,62,54,46,38,30,22,14,6,61,53,45,37,29,21,13,5,28,20,12,4]
PC2 = [14,17,11,24,1,5,3,28,15,6,21,10,23,19,12,4,26,8,16,7,27,20,13,2,41,52,31,37,47,55,30,40,51,45,33,48,44,49,39,56,34,53,46,42,50,36,29,32]
SHIFT = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]

# ----------------------
# Utilities
# ----------------------
def permute(block, table):
    return [block[i-1] for i in table]

def left_shift(block, n):
    return block[n:] + block[:n]
    #block[n:] → Takes the bits from position n to the end
    #block[:n] → Takes the first n bits.
    #Result: The bits are rotated left by n positions (
        #circular shift, not just padding zeros).

def xor_bits(a, b):
    return [x ^ y for x, y in zip(a, b)]

def bytes_to_bits(b):
    return [int(bit) for byte in b for bit in format(byte, '08b')]

def bits_to_bytes(bits):
    return bytes(int(''.join(map(str, bits[i:i+8])), 2) for i in range(0, len(bits), 8))

# ----------------------
# Key schedule & F-function
# ----------------------
def generate_keys(key_bits):
    key56 = permute(key_bits, PC1)            # 56 bits
    C, D = key56[:28], key56[28:]
    round_keys = []
    for s in SHIFT:
        C = left_shift(C, s)
        D = left_shift(D, s)
        round_keys.append(permute(C + D, PC2))  # 48 bits
    return round_keys

def feistel(R, subkey):
    expanded = permute(R, E)                # 48 bits
    xored = xor_bits(expanded, subkey)
    output_32 = []
    for i in range(8):
        block6 = xored[i*6:(i+1)*6]
        row = (block6[0] << 1) | block6[5]
        col = int(''.join(map(str, block6[1:5])), 2)
        val = S_BOX[i][row][col]
        output_32.extend([int(bit) for bit in format(val, '04b')])
    return permute(output_32, P)

# ----------------------
# Core DES block (encrypt/decrypt single 64-bit block)
# ----------------------
def des_block(block64_bits, round_keys, encrypt=True):
    block = permute(block64_bits, IP)
    L, R = block[:32], block[32:]
    keys = round_keys if encrypt else round_keys[::-1]
    for k in keys:
        newR = xor_bits(L, feistel(R, k))
        L = R
        R = newR
    preoutput = R + L
    return permute(preoutput, FP)

# ----------------------
# Padding (PKCS#5 / PKCS#7 for 8-byte block)
# ----------------------
def pad_pkcs5(data: bytes) -> bytes:
    pad_len = 8 - (len(data) % 8)
    return data + bytes([pad_len]) * pad_len

def unpad_pkcs5(data: bytes) -> bytes:
    if not data:
        return data
    pad_len = data[-1]
    if pad_len < 1 or pad_len > 8:
        raise ValueError("Invalid padding")
    return data[:-pad_len]

# ----------------------
# CBC mode wrappers
# ----------------------
def des_encrypt_cbc(plaintext: bytes, key: bytes, iv: bytes) -> bytes:
    if len(key) != 8 or len(iv) != 8:
        raise ValueError("Key and IV must be 8 bytes each")
    pt = pad_pkcs5(plaintext)
    pt_bits = bytes_to_bits(pt)
    iv_bits = bytes_to_bits(iv)
    key_bits = bytes_to_bits(key)
    round_keys = generate_keys(key_bits)

    cipher_bits = []
    for i in range(0, len(pt_bits), 64):
        block = pt_bits[i:i+64]
        # XOR with IV / previous ciphertext
        x = xor_bits(block, iv_bits)
        enc_block = des_block(x, round_keys, encrypt=True)
        cipher_bits.extend(enc_block)
        iv_bits = enc_block  # chain
    return bits_to_bytes(cipher_bits)

def des_decrypt_cbc(ciphertext: bytes, key: bytes, iv: bytes) -> bytes:
    if len(key) != 8 or len(iv) != 8:
        raise ValueError("Key and IV must be 8 bytes each")
    ct_bits = bytes_to_bits(ciphertext)
    iv_bits = bytes_to_bits(iv)
    key_bits = bytes_to_bits(key)
    round_keys = generate_keys(key_bits)

    plain_bits = []
    for i in range(0, len(ct_bits), 64):
        block = ct_bits[i:i+64]
        dec_block = des_block(block, round_keys, encrypt=False)
        # XOR decrypted block with IV/previous ciphertext
        plain_block = xor_bits(dec_block, iv_bits)
        plain_bits.extend(plain_block)
        iv_bits = block  # previous ciphertext becomes IV for next
    plaintext_padded = bits_to_bytes(plain_bits)
    return unpad_pkcs5(plaintext_padded)

# ----------------------
# Example usage
# ----------------------
if __name__ == "__main__":
    key = b'8bytekey'            # exactly 8 bytes
    iv  = b'12345678'            # exactly 8 bytes (in real use pick random)
    message = b"Hello DES CBC! This is 2-blocks long.."

    print("Plaintext:", message)
    ct = des_encrypt_cbc(message, key, iv)
    print("Ciphertext (hex):", ct.hex())

    pt = des_decrypt_cbc(ct, key, iv)
    print("Decrypted:", pt)
