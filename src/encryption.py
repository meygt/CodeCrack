# encryption.py

def caesar_encrypt(text, shift):
    encrypted = ''
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            shift_base = ord('A') if char.isupper() else ord('a')  # Handle upper and lower case
            encrypted += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted += char  # Non-alphabet characters are added without change
    return encrypted

def caesar_decrypt(encrypted_text, shift):
    return caesar_encrypt(encrypted_text, -shift)  # Decryption is just the reverse of encryption
