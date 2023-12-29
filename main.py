def kamasutra_cipher(plaintext, key1, key2):
    # Create a dictionary to map each letter to its corresponding letter from the opposite key
    cipher_map = dict(zip(key1, key2))

    # Encrypt the plaintext using the cipher map
    ciphertext = ''.join(cipher_map.get(char, char) for char in plaintext.lower())

    return ciphertext

# Example usage:
plaintext_input = input("Enter the plaintext: ")
key1 = 'wirlzubjqycvf axdmtesnpgokh'
key2 = 'axdmtesnpgokh wirlzubjqycvf'
encrypted_text = kamasutra_cipher(plaintext_input, key1, key2)
print("Encrypted Text:", encrypted_text)
