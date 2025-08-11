# 1. Caesar Cipher

def caesar_encrypt(text):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    key = ['d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c']
    lowercase_text = text.lower()
    encrypted_text = ''
    for char in lowercase_text:
        if char in alphabet:
            index = alphabet.index(char)
            encrypted_text += key[index]
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(text):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    key = ['d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c']
    lowercase_text = text.lower()
    decrypted_text = ''
    for char in lowercase_text:
        if char in key:
            index = key.index(char)
            decrypted_text += alphabet[index]
        else:
            decrypted_text += char
    return decrypted_text


# 2. Simple Columnar Cipher

def columnar_encrypt(plaintext, key):
    plaintext = plaintext.replace(" ", "")
    num_cols = len(key)
    num_rows = len(plaintext) // num_cols
    if len(plaintext) % num_cols != 0:
        num_rows += 1
    matrix = [['' for _ in range(num_cols)] for _ in range(num_rows)]
    index = 0
    for r in range(num_rows):
        for c in range(num_cols):
            if index < len(plaintext):
                matrix[r][c] = plaintext[index]
                index += 1
    key_order = [int(k) - 1 for k in key]
    ciphertext = ""
    for col in key_order:
        for row in range(num_rows):
            if matrix[row][col] != '':
                ciphertext += matrix[row][col]
    return ciphertext

def columnar_decrypt(ciphertext, key):
    num_cols = len(key)
    num_rows = len(ciphertext) // num_cols
    if len(ciphertext) % num_cols != 0:
        num_rows += 1
    key_order = [int(k) - 1 for k in key]
    col_lengths = [num_rows] * num_cols
    extra_spaces = num_cols * num_rows - len(ciphertext)
    for i in range(extra_spaces):
        col_lengths[key_order[-(i + 1)]] -= 1
    matrix = [['' for _ in range(num_cols)] for _ in range(num_rows)]
    index = 0
    for col in key_order:
        for row in range(col_lengths[col]):
            matrix[row][col] = ciphertext[index]
            index += 1
    plaintext = ""
    for row in matrix:
        plaintext += ''.join(row)
    return plaintext


# 3. Rail Fence Cipher (Simple)

def rail_fence_encrypt(text, rails):
    fence = ['' for _ in range(rails)]
    rail = 0
    direction = 1
    for char in text:
        fence[rail] += char
        rail += direction
        if rail == 0 or rail == rails - 1:
            direction *= -1
    return ''.join(fence)

def rail_fence_decrypt(ciphertext, rails):
    pattern = list(range(rails)) + list(range(rails - 2, 0, -1))
    rail_indices = [pattern[i % len(pattern)] for i in range(len(ciphertext))]
    rail_lengths = [rail_indices.count(r) for r in range(rails)]
    rails_content = []
    index = 0
    for length in rail_lengths:
        rails_content.append(list(ciphertext[index:index+length]))
        index += length
    result = ""
    for r in rail_indices:
        result += rails_content[r].pop(0)
    return result



# Choice

def main():
    while True:
        print("\n Encryption/Decryption Tool ")
        print("1. Caesar Cipher")
        print("2. Simple Columnar Cipher")
        print("3. Rail Fence Cipher")
        print("4. Exit")
        choice = input("Choose algorithm (1-4): ")

        if choice == '4':
            print("Exiting...")
            break

        text = input("Enter text: ")
        mode = input("Encrypt or Decrypt? (e/d): ").lower()

        if choice == '1':  # Caesar Cipher
            if mode == 'e':
                print("Encrypted:", caesar_encrypt(text))
            elif mode == 'd':
                print("Decrypted:", caesar_decrypt(text))

        elif choice == '2':  # Columnar Cipher
            key = input("Enter numeric key (e.g., 1432): ")
            if mode == 'e':
                print("Encrypted:", columnar_encrypt(text, key))
            elif mode == 'd':
                print("Decrypted:", columnar_decrypt(text, key))

        elif choice == '3':  # Rail Fence Cipher
            rails = int(input("Enter number of rails: "))
            if mode == 'e':
                print("Encrypted:", rail_fence_encrypt(text, rails))
            elif mode == 'd':
                print("Decrypted:", rail_fence_decrypt(text, rails))

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
