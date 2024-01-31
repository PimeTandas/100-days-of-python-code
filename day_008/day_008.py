# Ceasar Cipher

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def ceaser(text, shift, direction):
    new = ""
    if direction == "encode":
        shift = shift
    elif direction == "decode":
        shift = -shift

    for letter in text:
        index = alphabet.index(letter) + shift
        if index > 25:
            index -= 26
        new += alphabet[index]

    print(f"New message is {new}")

ceaser(text, shift, direction)