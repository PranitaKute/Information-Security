# 2. Simple Columnar Algorithm

# In this algorithm we arrange the plaintext in rows, columns based on the key, for ex. key is 1 2 3 4, so 4 columns.
# For cipher text read the plain text by columns give by sequence, for ex. 2 4 1 3. This will be the cipher text.

def columnar_encrypt(plaintext, key):
    # Remove spaces from plaintext
    plaintext = plaintext.replace(" ", "")
    
    # Number of columns
    num_cols = len(key)
    
    # Calculate number of rows
    num_rows = len(plaintext)  // num_cols
    if len(plaintext) % num_cols != 0:
        num_rows += 1  # Add extra row for leftover characters
    
    # Fill the matrix row-wise
    matrix = [['' for _ in range(num_cols)] for _ in range(num_rows)]
    index = 0
    for r in range(num_rows):
        for c in range(num_cols):
            if index < len(plaintext):
                matrix[r][c] = plaintext[index]
                index += 1
    
    # Convert key to numeric order mapping (1-based)
    key_order = [int(k) - 1 for k in key]
    
    # Read columns in the order given by the key
    ciphertext = ""
    for col in key_order:
        for row in range(num_rows):
            if matrix[row][col] != '':
                ciphertext += matrix[row][col]
    
    return ciphertext

# Example usage
message = input("Enter plaintext to encrypt: ")
key = input("Enter numeric key (e.g., 1432): ")
cipher = columnar_encrypt(message, key)
print("Ciphertext:", cipher)
