# Ceasar Cipher

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
    new = ""
    for letter in text:
        index = alphabet.index(letter) + shift
        if index > 25:
            index -= 26
        new += alphabet[index]
    print(f"The encoded text is {new}")


def decrypt(text, shift):
    new = ""
    for letter in text:
        index = (alphabet.index(letter)) - shift
        new += alphabet[index]
    print(f"The decoded text is {new}")


if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)
else:
    print("You did not select a valid option.")