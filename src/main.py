# main.py

from encryption import caesar_encrypt, caesar_decrypt

def test_caesar_cipher():
    original_text = "Hello, World!"
    shift = 3
    encrypted_text = caesar_encrypt(original_text, shift)
    decrypted_text = caesar_decrypt(encrypted_text, shift)

    print(f"Original: {original_text}")
    print(f"Encrypted: {encrypted_text}")
    print(f"Decrypted: {decrypted_text}")

if __name__ == "__main__":
    test_caesar_cipher()
