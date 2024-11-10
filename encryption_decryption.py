def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted_text += chr((ord(char) + shift - shift_base) % 26 + shift_base)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    return encrypt(text, -shift)

message = input("Enter a message to encrypt: ")
shift_value = int(input("Enter shift value: "))
encrypted_message = encrypt(message, shift_value)
print("Encrypted Message:", encrypted_message)
print("Decrypted Message:", decrypt(encrypted_message, shift_value))
