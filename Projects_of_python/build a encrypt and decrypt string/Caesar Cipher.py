def caesar(text, shift, encrypt=True):

    if not isinstance(shift, int):
        return 'Shift must be an integer value.'

    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    if not encrypt:
        shift = -shift

    shifted_alphabet = alphabet[shift:] + alphabet[:shift]

    translation_table = str.maketrans(
        alphabet + alphabet.upper(),
        shifted_alphabet + shifted_alphabet.upper()
    )

    return text.translate(translation_table)


def encrypt(text, shift):
    return caesar(text, shift, encrypt=True)


def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)


choice = input("Type 'e' to encrypt or 'd' to decrypt: ").lower()
text = input("Enter your text: ")
shift = int(input("Enter shift value (1–25): "))

if choice == 'e':
    result = encrypt(text, shift)
    print("Encrypted Text:", result)

elif choice == 'd':
    result = decrypt(text, shift)
    print("Decrypted Text:", result)

else:
    print("Invalid choice! Please type 'e' or 'd'.")
