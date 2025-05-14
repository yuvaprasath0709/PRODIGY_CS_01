def caesar_cipher(text, shift, mode):
    """
    Encrypts or decrypts text using the Caesar Cipher algorithm.

    Args:
        text (str): The text to be processed.
        shift (int): The number of positions to shift each letter.
        mode (str): 'encrypt' or 'decrypt'.

    Returns:
        str: The encrypted or decrypted text.
    """
    result = ''
    for char in text:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            shifted_char_code = (ord(char) - start + (shift if mode == 'encrypt' else -shift)) % 26 + start
            result += chr(shifted_char_code)
        elif char.isdigit():
            shifted_digit = (int(char) + (shift if mode == 'encrypt' else -shift)) % 10
            result += str(shifted_digit)
        else:
            result += char
    return result

def main():
    """
    Controls the flow of the program, handling user input and calling
    the encryption/decryption functions.
    """
    while True:
        try:
            choice = input("Do you want to encrypt (e), decrypt (d), or quit (q)? ").lower()
        except EOFError:
            print("\nInput interrupted. Exiting.")
            break  # Exit the loop if input is interrupted

        if choice == 'q':
            break
        elif choice in ('e', 'd'):
            message = input("Enter your message: ")
            while True:
                try:
                    shift = int(input("Enter the shift value (integer): "))
                    break
                except ValueError:
                    print("Invalid input. Please enter an integer for the shift value.")
                except EOFError:
                    print("\nInput interrupted. Exiting.")
                    return  # Exit the function if input is interrupted

            if choice == 'e':
                ciphertext = caesar_cipher(message, shift, 'encrypt')
                print("Ciphertext:", ciphertext)
            elif choice == 'd':
                plaintext = caesar_cipher(message, shift, 'decrypt')
                print("Plaintext:", plaintext)
        else:
            print("Invalid choice. Please enter 'e', 'd', or 'q'.")

if __name__ == "__main__":
    main()

