# Encryption & Decryption Algorithms

# 1. Caesar Cipher
# key = int(input("Enter key for Caesar Cipher"))
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# default key = 3
key = ['d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',  'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c']
text = input("Enter Message to Encrypt : ")

# Search index of character and print its value from key at same index
lowercase_text = text.lower()


encrypted_text = ''
for char in lowercase_text:
    if char in alphabet:
        index = alphabet.index(char)
        encrypted_text += key[index]
    else:
        # Keep non-alphabet characters unchanged (e.g., space, punctuation)
        encrypted_text += char

print("Encrypted Message:", encrypted_text)
