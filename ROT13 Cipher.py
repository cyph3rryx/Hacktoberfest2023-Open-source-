import base64
import sys

def encrypt_rot13(text):
    encrypted_text = ""
    for char in text:
        if 'a' <= char <= 'z':
            offset = ord('a')
            encrypted_text += chr((ord(char) - offset + 13) % 26 + offset)
        elif 'A' <= char <= 'Z':
            offset = ord('A')
            encrypted_text += chr((ord(char) - offset + 13) % 26 + offset)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt_rot13(encrypted_text):
    return encrypt_rot13(encrypted_text)  # ROT13 is its own inverse

def main():
    print("Cipher Tool (ROT13 and Base64)")

    while True:
        choice = input("Do you want to (E)ncrypt, (D)ecrypt, or (Q)uit? ").upper()

        if choice == 'Q':
            print("Goodbye!")
            sys.exit(0)
        elif choice == 'E':
            sub_choice = input("Encrypt with (R)OT13 or (B)ase64? ").upper()
            plaintext = input("Enter the text: ")

            if sub_choice == 'R':
                encrypted_text = encrypt_rot13(plaintext)
                print("Encrypted text:", encrypted_text)
            elif sub_choice == 'B':
                encrypted_bytes = base64.b64encode(plaintext.encode())
                encrypted_text = encrypted_bytes.decode()
                print("Base64 encoded:", encrypted_text)
            else:
                print("Invalid choice.")
        elif choice == 'D':
            sub_choice = input("Decrypt (R)OT13 or (B)ase64? ").upper()
            encrypted_text = input("Enter the encrypted text: ")

            if sub_choice == 'R':
                decrypted_text = decrypt_rot13(encrypted_text)
                print("Decrypted text:", decrypted_text)
            elif sub_choice == 'B':
                try:
                    encrypted_bytes = base64.b64decode(encrypted_text)
                    decrypted_text = encrypted_bytes.decode()
                    print("Base64 decoded:", decrypted_text)
                except:
                    print("Invalid Base64 input.")
            else:
                print("Invalid choice.")
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
