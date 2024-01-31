# Ceasar Cipher

from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
run_program = True
print(logo)

def ceaser(start_text, shift_amount, cipher_direction):
    new_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for _ in start_text:
        if _ in alphabet:
            index = alphabet.index(_) + shift_amount
            if index > 25:
                index -= 26
                print(index)
            new_text += alphabet[index]
        else:
            new_text += _
    print(f"The final {cipher_direction}ed message is {new_text}")


while run_program:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift_new = shift % 26
    print(shift_new)
    ceaser(text, shift_new, direction)

    continue_program = input("Would you like to encode another message? (0) for Yes or (1) for No: ")
    if continue_program == "1":
        run_program = False
        print("Exiting Program")